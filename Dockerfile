FROM python
WORKDIR /app
COPY requirements.txt /app/
COPY app.py /app/
RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8501
CMD ["streamlit","run","app.py"]