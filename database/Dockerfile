#------------------------ Dockerfile ---------------------------------------#
# Use the official PostgreSQL image from the Docker Hub
FROM postgres:latest

# Set environment variables for the database
ENV POSTGRES_DB=mydatabase
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword

# Expose the default PostgreSQL port
EXPOSE 5432

# Copy custom initialization scripts to the container's initialization directory
COPY init.sql /docker-entrypoint-initdb.d/

# Copy custom configuration files to the container
COPY pg_hba.conf /etc/postgresql/
COPY environment /etc/postgresql/
COPY pg_ctl.conf /etc/postgresql/
COPY pg_ident.conf /etc/postgresql/
COPY postgresql.conf /etc/postgresql/
COPY start.conf /etc/postgresql/

# Set the default command to run when starting the container
CMD ["postgres"]