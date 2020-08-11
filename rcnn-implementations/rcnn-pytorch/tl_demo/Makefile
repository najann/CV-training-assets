app_name = tl-demo
heroku_name = $(app_name)$$(date +'%Y%m%d-%H')

build:
	@docker build -t $(app_name) .

run:
	-@docker stop $(app_name)
	-@docker rm $(app_name)
	@docker run --detach -p 5000:5000 --name $(app_name) $(app_name)

kill:
	@echo 'Killing container...'
	@docker stop $(app_name)
	@docker rm $(app_name)

herokup:
	@heroku create $(heroku_name)
	@heroku container:push web --app $(heroku_name)
	@heroku container:release web --app $(heroku_name)
	@heroku open --app $(heroku_name)