# Start from a Miniconda base image
FROM continuumio/miniconda3

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file for better caching
COPY requirements.txt .

# Create a conda environment called python-api, install Flask and other Python dependencies
RUN conda create -n python-api python=3.10 flask --yes && \
    conda install -n python-api --file requirements.txt --solver=classic --yes && \
    conda clean -afy

# Install R, rpy2, and necessary system dependencies in the same Conda environment
RUN conda install -n python-api -c conda-forge r-base rpy2 r-devtools libcurl libxml2 --solver=classic --yes && \
    conda clean -afy

# Install PCAmixdata within the conda R environment
RUN conda run -n python-api R -e "install.packages('PCAmixdata', repos='https://cloud.r-project.org')"

# Set the environment path to the conda environment
ENV PATH /opt/conda/envs/python-api/bin:$PATH

# Optional: Set R_HOME for rpy2 if needed
# ENV R_HOME /opt/conda/envs/python-api/lib/R

# Expose the port that Flask will run on
EXPOSE 5000

# Copy the rest of the application code
COPY . .

# Activate the environment and run the Flask application
CMD ["conda", "run", "-n", "python-api", "flask", "run", "--host", "0.0.0.0"]