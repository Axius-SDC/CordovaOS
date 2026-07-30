# CordovaOS — clone-and-run reference implementation.
#
# Requirements: Docker (or Podman) with the compose plugin, ~6GB free RAM, and
# Python 3.12 on the host (for data generation only).
#
# Typical first run:
#   make demo      # start the stack, generate the small dataset, load it
# then open http://localhost:18000/demo/

COMPOSE := docker compose -f app/sdc4/docker-compose.yml
WEB_URL  := http://localhost:18000

.PHONY: help up down demo demo-full generate generate-full load wait-web clean

help:
	@echo "CordovaOS quickstart:"
	@echo "  make demo        Start the stack + generate + load the SMALL demo dataset"
	@echo "                   (~1,500 records, a few minutes). The default."
	@echo "  make demo-full   Same, but the FULL 25,000-resident dataset"
	@echo "                   (~100K records; generation is seconds, loading takes HOURS)."
	@echo "  make up          Start the stack only."
	@echo "  make down        Stop the stack."
	@echo "  make clean       Stop the stack and remove generated import data."
	@echo ""
	@echo "After 'make demo', open $(WEB_URL)/demo/"

up:
	$(COMPOSE) up -d

down:
	$(COMPOSE) down

# Wait until the web app answers before loading (first run migrates + inits GraphDB).
wait-web:
	@echo "Waiting for the web app at $(WEB_URL) (first run can take 1-2 min)..."
	@until curl -sf $(WEB_URL)/ >/dev/null 2>&1; do sleep 3; done
	@echo "Web app is up."

# Generation runs on the host (Python 3.12 + cuid2); writes app/sdc4/import_data/.
generate:
	@python3 -m pip install -q -r datagen/requirements.txt
	cd datagen && CORDOVA_DEMO_SCALE=1 python3 generate_all.py

generate-full:
	@python3 -m pip install -q -r datagen/requirements.txt
	cd datagen && python3 generate_all.py

# Loading runs in the web container (validates each instance, writes Postgres + GraphDB).
load: wait-web
	$(COMPOSE) exec -T web python manage.py load_all_data --clear

demo: up generate load
	@echo ""
	@echo "Demo ready. Open $(WEB_URL)/demo/"

demo-full: up generate-full load
	@echo ""
	@echo "Full dataset ready. Open $(WEB_URL)/demo/"

clean:
	$(COMPOSE) down
	@find app/sdc4/import_data -mindepth 1 -maxdepth 1 -type d -exec rm -rf {} + 2>/dev/null || true
	@echo "Stack stopped and generated import data removed."
