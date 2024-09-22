FROM python:3.10
FROM continuumio/miniconda3

WORKDIR /app
RUN pip install flask

# Create a conda environment called python-api and install Flask
RUN conda create -n python-api python=3.10 flask && \
    conda clean -afy

# Activate the environment and set it as the default
ENV PATH /opt/conda/envs/python-api/bin:$PATH

EXPOSE 5000

COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]