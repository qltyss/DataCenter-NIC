import cv2
import numpy as np
import pyrealsense2 as rs
from threading import Thread, Lock
import time
import logging

class CameraStream:
    def __init__(self, max_retries=10, retry_delay=5, log_file='camerastream.log'):
         # Set up logging
        self.logger = logging.getLogger('CameraStream')
        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.setLevel(logging.DEBUG)  # Set logging level to DEBUG

        # Initialize the RealSense pipeline
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
        self.config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

        self.pipeline_started = False
        try:
            self.pipeline.start(self.config)
            self.pipeline_started = True
        except Exception as e:
            self.logger.error(f"Error initializing RealSense pipeline: {e}")
            self.pipeline_started = False
            raise

        self.stopped = False
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.lock = Lock()
        self.latest_color_frame = None
        self.latest_depth_frame = None

    def start(self):
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        while True:
            if self.stopped:
                return

            try:
                frames = self.pipeline.wait_for_frames()
                depth_frame = frames.get_depth_frame()
                color_frame = frames.get_color_frame()

                if not frames:

                    self.logger.warning("Failed to grab frame. Attempting to reconnect...")
                    self.reconnect()
                
                    

                depth_image = np.asanyarray(depth_frame.get_data())
                color_image = np.asanyarray(color_frame.get_data())
                depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)
                with self.lock:
                    self.latest_color_frame = color_image
                    self.latest_depth_frame = depth_colormap

            except Exception as e:
                
                self.logger.error(f"Error during frame update: {e}")
                self.reconnect()

    def reconnect(self):
        retries = 0
        while retries < self.max_retries:
            with self.lock:
                if self.pipeline_started:
                    try:
                        self.pipeline.stop()
                    except Exception as e:
                        self.logger.error(f"Error stopping the pipeline during reconnection: {e}")
                    self.pipeline_started = False

                time.sleep(self.retry_delay)
                try:
                    self.pipeline.start(self.config)
                    self.pipeline_started = True
                    self.logger.info("Reconnected successfully!")
                    return
                except Exception as e:
                    self.pipeline_started = False
                    self.logger.error(f"Error during reconnection: {e}")

                retries += 1
                self.logger.warning(f"Reconnect attempt {retries} failed.")

        self.logger.error("Max reconnect attempts reached. Stopping stream.")
        self.stop()

    def read_color(self):
        return self.latest_color_frame

    def read_depth(self):
        return self.latest_depth_frame

    def stop(self):
        with self.lock:
            if self.pipeline_started:
                try:
                    self.pipeline.stop()
                except Exception as e:
                    self.logger.error(f"Error while stopping the pipeline: {e}")
                self.pipeline_started = False

# Create and start the camera stream
camera_stream = CameraStream()
camera_stream.start()

