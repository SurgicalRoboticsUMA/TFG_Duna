## Class Camera ##

# Libraries #
import pyrealsense2 as rs
import numpy as np
import math

class Camera:
    ## Parameters: resolution (height, width), pipeline, config, align

    """ Inicialize the camera """
    def init_camera(self):
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.align = rs.align(rs.stream.color)
        # Start streaming
        self.pipeline.start(self.config)
    
    """ Stablish the resolution of the camera """
    def set_resolution(self, h, w):
        self.height = h
        self.width = w

    """ Stop the streaming """
    def finalize(self):
        self.pipeline.stop()

    """ Set scale of the image """
    def set_scale (self, distance):
        return math.trunc(distance * 1000 / 12)

    """ Obtain the distance of the frames given """
    def get_distance(self, frames, width, height):
        dis = frames.get_distance(int(round(width / 2)), int(round(height / 2)))
        i = 1
        while dis == 0:
            dis = frames.get_distance(int(round(width / 2 + i)), int(round(height / 2 + i)))
            i +=1
        return dis * 100

    """ Detecting death_zones with the manual formula """
    def death_zones(self, distance, width):
        ratio = 0.18 / (2 * distance * math.tan((84*math.pi)/(2*180)))
        pixels = math.trunc(width * ratio)
        return pixels

    """ Obtainig the align from de camera """
    def get_align(self):
        # Get device product line for setting a supporting resolution
        pipeline_wrapper = rs.pipeline_wrapper(self.pipeline)
        pipeline_profile = self.config.resolve(pipeline_wrapper)
        device = pipeline_profile.get_device()

        # Enabling camera stream from the configuration
        self.config.enable_stream(rs.stream.depth, self.width, self.height, rs.format.z16, 30)
        self.config.enable_stream(rs.stream.color, self.width, self.height, rs.format.bgr8, 30)

        # Wait for a coherent pair of frames: depth and color
        frames = self.pipeline.wait_for_frames()

        # Aligned_depth_frame is a 640x480 depth image
        aligned_depth_frame = frames.get_depth_frame() 
        color_frame = frames.get_color_frame()

        return aligned_depth_frame, color_frame

    """ Obtain the depth image """
    def get_image (self, aligned_depth_frame, color_frame):
        # Convert images to numpy arrays
        depth_image = np.asanyarray(aligned_depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        # Generates color images based on input depth frame
        colorizer = rs.colorizer()
        depth_colormap = np.asanyarray(colorizer.colorize(aligned_depth_frame).get_data())
        depth_intrinsics =  aligned_depth_frame.profile.as_video_stream_profile().intrinsics
            
        return depth_colormap, color_image, depth_intrinsics, depth_image
