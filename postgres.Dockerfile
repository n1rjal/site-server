# Use PostgreSQL 15 as the base image
FROM postgres:15

# Switch to root to make permission changes
USER root

# Adjust permissions on the PostgreSQL directories
RUN mkdir -p /var/lib/postgresql/data \
    && mkdir -p /var/run/postgresql \
    && chown -R 0:0 /var/lib/postgresql /var/run/postgresql \
    && chmod -R g=u /var/lib/postgresql /var/run/postgresql

# Set the default user back to postgres
USER postgres

# Set the environment variable to use a subdirectory for PGDATA
ENV PGDATA=/var/lib/postgresql/data/pgdata

# Expose the PostgreSQL port
EXPOSE 5432

# Default command to start the PostgreSQL server
CMD ["postgres"]
