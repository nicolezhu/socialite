# import click

# @click.command()
# @click.option('--name', prompt='Your name')

# def hello(name):
# 	click.echo('Hello %s!' % name)


import sys

def hello():
	name = raw_input('Enter your name: ')
	print ("hello " + name)

if __name__ == '__main__':
	hello()