# Plan 

1) Track flow with image-space motion vectors
    - structure from motion
2) Filter Non-static Objects
   - Static objects will have coherent and consistent motion
   - Can remove outliers for this case
   - RANSAC (simple enough through 3d space)
   - maybe segment foreground/background?
3) Calculate direction vector
   - normalize static vectors and invert direction for angle
   - Recover direction vector and compute pitch/yaw


## General Attack Process

FrameReader → FeatureTracker → MotionEstimator → DirectionCalculator → LabelWriter