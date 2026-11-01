
FROM quay.io/jupyter/datascience-notebook:latest

USER root

# plan to mount license at runtime
ENV GRB_LICENSE_FILE=/opt/gurobi/gurobi.lic

# create license directory
RUN mkdir -p /opt/gurobi && chown ${NB_UID}:${NB_GID} /opt/gurobi

# Install gurobi, mySQL libraries, and redis 
RUN pip install --no-cache-dir \
    gurobipy==13.0.1 \
    pymysql \
    sqlalchemy \
    redis

USER ${NB_UID}

# Set the default working directory
WORKDIR /home/jovyan/iem4723

# Jupyter listens on 8888 in container & maps to 4444 on localhost in compose file
EXPOSE 8888
CMD ["start-notebook.sh"]
