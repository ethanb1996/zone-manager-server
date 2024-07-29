# zone-manager-server

    Description:
    - The api reveals three routes that perform action on a csv file: 
        /create_zone : add a new zone
        /delete_zone/{id} : delete a zone by its id
        /all_zones : fetch all the zones


# How to run the api?

1. Build the container: docker build -t <container_name> .
2. Run The container: docker run -d -p 8000:8000 <container_name>