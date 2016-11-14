# Halo Filebeat
## Ships Halo logs to ELK via Filebeat protocol

Note: This is only for testing (think docker-compose).  As it DOES NOT implement encryption between itself and the Logstash server, don't do anything with it where encryption of transmissions is required.

Set these environment variables:

| var                 | purpose                        |
|---------------------|--------------------------------|
| HALO_API_KEY        | API key for Halo               |
| HALO_API_SECRET_KEY | API secret for Halo            |
| LOGSTASH_HOST       | host and port, colon-delimited |

Run it like this:

`docker run -it --rm -e HALO_API_KEY=$HALO_API_KEY -e HALO_API_SECRET_KEY=$HALO_API_SECRET_KEY -e LOGSTASH_HOST=$LOGSTASH_HOST --name halo_beat halo_beat `

On exit, it will note the timestamp from the last event captured.
