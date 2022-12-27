FROM python:3.8

# Install the required packages
COPY ./requirements.txt /app    
RUN pip install -r requirements.txt

# Copy the frontend code to the container
COPY . .

# Expose port 8001
EXPOSE 8001

# Run the frontend
CMD ["streamlit", "run", "app.py", "--server.port", "8001"]
