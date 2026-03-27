# Robotic Hand Vision System

A real-time computer vision system that tracks hand motion, extracts finger joint angles, and visualizes them for robotic control applications.

## Overview

This project uses computer vision to detect hand landmarks and compute finger joint angles in real time. The system is designed as a foundation for controlling a robotic hand using natural human motion.

The pipeline includes:
- Hand detection using MediaPipe
- Joint angle estimation using vector math
- Real-time visualization through a custom UI

## Features

- Real-time hand tracking
- 21-point landmark detection
- Finger angle calculation (0°–180°)
- Interactive UI dashboard
- Modular architecture for hardware integration

## System Architecture

Camera → Hand Detection → Landmark Extraction → Angle Computation → UI Visualization

## Finger Angle Calculation

Joint angles are computed using vector geometry between three landmarks:
θ = cos⁻¹((BA · BC) / (|BA||BC|))
This allows continuous estimation of finger bending for realistic motion mapping.

## UI Preview
<img width="500" height="349" alt="image" src="https://github.com/user-attachments/assets/17586301-8f83-46b4-8d30-064010b5b0a7" />

## Future Work

- Integration with servo motors for physical robotic hand control
- Wrist degree-of-freedom tracking
- Gesture recognition system
- ASL (American Sign Language) generation
- Sensor fusion with IMU for improved accuracy
- Improved UI with hand model to make the angel calculation more eas to interpert

## What I Learned

- Real-time computer vision pipelines
- Kinematic modeling using vector math
- Signal smoothing and noise handling
- Designing modular robotics systems


