from api import APP
from api.db import QUERIES


def get_region_port_codes(slug: str):
    """Given a region slug, get a list of all port codes within the region"""
    cur = APP.db_conn.cursor()

    # get a list of region slugs for the current region and all children
    query = QUERIES["get_region_children"].format(slug=slug)
    APP.logger.debug("\n" + query)

    cur.execute(query)
    slugs = [row[0] for row in cur.fetchall()]

    # use the list of slugs to get a list of port codes
    query = QUERIES["get_region_ports"].format(
        slugs=", ".join([f"'{slug}'" for slug in slugs])
    )
    APP.logger.debug("\n" + query)

    cur.execute(query)
    port_codes = [row[0] for row in cur.fetchall()]

    cur.close()

    return port_codes
