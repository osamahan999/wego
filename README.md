Install postgres using brew

`brew install postgresql   `

Start Postgres using

`brew services start postgresql@14`

To go into the PSQL console

`psql -d postgres`


In the psql console, run

`CREATE USER postgres SUPERUSER;`

`CREATE DATABASE wego WITH OWNER postgres;`
