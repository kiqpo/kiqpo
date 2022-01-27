#!/usr/bin/env python
from livereload import Server, shell
server = Server()
server.watch('kiqpo/native/', shell('make html', cwd='kiqpo'))
server.serve(root='./kiqpo/native')
