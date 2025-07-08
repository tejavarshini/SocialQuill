# SocialEcho

A social networking platform with automated content moderation and context-based authentication system.

[Watch Demo](https://youtu.be/Tmncayg7FeU)

![UI-community](https://raw.githubusercontent.com/nz-m/SocialEcho/main/resources/UI-community.png)

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies](#technologies)
- [Schema Diagram](#schema-diagram)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [License](#license)

## Project Overview

SocialQuill
SocialQuill is a full-stack social networking application built using the MERN stack, featuring AI-powered content moderation and context-based authentication for enhanced platform safety and user data integrity.

This project is a customized and extended version of SocialEcho, built to demonstrate full-stack engineering, system design, and applied AI integration.

Features
User authentication and role-based access (Admin, Moderator, General User)

Post creation, commenting, liking, and follow/unfollow functionality

Automated content moderation using:

Perspective API

TextRazor API

HuggingFace Zero-Shot Classification (via Flask service)

Context-based login tracking using IP address, device ID, and location

AES-encrypted device management and suspicious login alerts

Admin and Moderator dashboards for content and community control

Email notifications for authentication and account activity

Azure Blob Storage integration for secure file handling

Tech Stack
Frontend: React.js, Redux, Tailwind CSS
Backend: Node.js, Express.js, MongoDB, Flask
Authentication: JWT, Passport.js, CryptoJS
AI/NLP: HuggingFace Transformers, PyTorch
Deployment: Vercel / Render



## Features

- [x] User authentication and authorization (JWT)
- [x] User profile creation and management
- [x] Post creation and management
- [x] Commenting on posts
- [x] Liking posts and comments
- [x] Following/unfollowing users
- [x] Reporting posts
- [x] Content moderation
- [x] Context-based authentication
- [x] Device management
- [x] Admin dashboard
- [x] Moderator dashboard
- [x] Email notifications


## Technologies

- React.js
- Redux
- Node.js
- Express.js
- MongoDB
- Tailwind CSS
- JWT Authentication
- Passport.js
- Nodemailer
- Crypto-js
- Azure Blob Storage
- Flask
- Hugging Face Transformers


## Schema Diagram

![Schema Diagram](https://raw.githubusercontent.com/nz-m/SocialEcho/main/resources/Schema-Diagram.png)




