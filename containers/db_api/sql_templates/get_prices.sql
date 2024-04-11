SELECT * FROM prices
    WHERE
	(orig_code IN ({origins}) AND dest_code IN ({destinations}))
	AND
	(day>='{date_from}' AND day<='{date_to}');
