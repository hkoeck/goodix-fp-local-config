# COPR "make srpm" entry point: pack the repo and build the SRPM.
NAME = goodix-fp-local-config
VERSION = 1
outdir ?= $(CURDIR)

srpm:
	rm -rf /tmp/$(NAME)-$(VERSION)
	mkdir -p /tmp/$(NAME)-$(VERSION)
	cp -r rules rpm /tmp/$(NAME)-$(VERSION)/
	tar -C /tmp -czf "$(outdir)/$(NAME)-$(VERSION).tar.gz" $(NAME)-$(VERSION)
	rpmbuild -bs rpm/$(NAME).spec \
	  --define "_sourcedir $(outdir)" \
	  --define "_srcrpmdir $(outdir)"
