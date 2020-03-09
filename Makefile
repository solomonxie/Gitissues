
install:
	cd ~
	mkdir -p ~/autobackup
	cd ~/autobackup
	git clone git@github.com:solomonxie/issues_blog.git
	# Copy configs
	cp -r ~/autobackup/issues_blog/.local/ ~/autobackup/issues_blog/.local
	cp .config.json ~/Gitissues/
	cd ~/autobackup/issues_blog
	git config user.name "TO BE FILLED"
	git config user.email "TO BE FILLED"
	# Add cronjobs
	echo "*/1 * * * * cd ~/Gitissues && python3 issues.py > ~/Gitissues/.gitissues.log 2>&1" |crontab
	tail -f ~/Gitissues/.gitissues.log
