# Update and install packages
FROM node:19-slim AS frontend
# Update package list and install necessary packages
RUN apt-get update
# Upgrade installed packages
RUN apt-get upgrade -y
# Install build tools, Git, Python, npm, and other dependencies
RUN apt-get install -y --no-install-recommends build-essential git python3-pip npm curl nodejs
# Clean up
RUN rm -rf /var/lib/apt/lists/*
RUN pip3 install setuptools
RUN pip3 install django djangorestframework markdown requests bs4 django-cors-headers
RUN mkdir /home/frontend
WORKDIR /home/frontend
RUN git clone -b Frontend https://github.com/RihaanBH-1810/auto_webpentest_tool.git /home/frontend
RUN npm install
EXPOSE 3000
WORKDIR /home/frontend
CMD  ["npm", "start"]
