upload:
	lftp -c "open -u ${CS_USERNAME},${CS_PASSWORD} ftp.club-silencio.com; set ssl:verify-certificate no; mirror -R ${PWD}/build/ /public_html"

trans_compile:
	pybabel compile -d translations

trans_init:
	pybabel init -i messages.pot -d translations -l pt_BR

trans_extract:
	pybabel extract -F babel.cfg -k lazy_gettext -o messages.pot .

trans_update:
	pybabel update -i messages.pot -d translations