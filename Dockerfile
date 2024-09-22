# Start from a Miniconda base image
FROM continuumio/miniconda3

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file first for better caching
COPY requirements.txt .

# Create a conda environment called python-api and install dependencies
RUN conda create -n python-api python=3.10 flask && \
    conda install -n python-api --file requirements.txt --solver=classic && \
    conda clean -afy

# Install R and rpy2 in the same environment
RUN conda install -n python-api -c conda-forge r-base rpy2 --solver=classic && \
    conda clean -afy

# Set R_HOME
# ENV R_HOME /opt/conda/envs/python-api/lib/R

# Optional: Force ABI mode for rpy2
# ENV RPY2_CFFI_MODE ABI

# Activate the environment and set it as the default
ENV PATH /opt/conda/envs/python-api/bin:$PATH

# Optionally, install other packages
#RUN conda install -n python-api -c conda-forge PCAmixdata --solver=classic && \
#    conda clean -afy

# Expose the port the app runs on
EXPOSE 5000

# Copy the rest of the application
COPY . .

# Command to run the Flask application
CMD ["flask", "run", "--host", "0.0.0.0"]