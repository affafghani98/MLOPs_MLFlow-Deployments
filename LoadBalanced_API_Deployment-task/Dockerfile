FROM python:3.8-slim

# Install dependencies
RUN pip install flask

# Copy your app code into the container
COPY app.py /app.py

# Expose port
EXPOSE 5000

# Set the working directory
WORKDIR /

# Run the app
CMD ["python", "app.py"]