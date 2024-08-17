
MAKE 	?= make
AWK		?= gawk

DOCDIR   := docs
SITEDIR	 := ../../docs
FAUSTLIBS ?= ../../
CONTRIBUTORS = docs/contributors


####################################################################
help:
	@echo "========================================================================"
	@echo "                     Faust Libraries Documentation"
	@echo "This Makefile is intended to generate the faust libraries documentation"
	@echo "========================================================================"
	@echo "Available targets are:"
	@echo "  install  : install the required components"
	@echo "  build    : build the web site"
	@echo "  serve    : launch the mkdoc server"
	@echo "Development specific targets are available:"
	@echo "  md       : build the md files"
	@echo "  clean    : removes the output of the md target"


####################################################################
build:
	$(MAKE) md
	mkdocs build

serve:
	@echo "you can browse the site at http://localhost:8000"
	mkdocs serve
	
clean:
	rm -rf $(CONTRIBUTORS)
	

####################################################################
# building md files
md : 
	python3 scripts/make_md.py $(FAUSTLIBS) $(DOCDIR) scripts/faustlib2md.awk
	python3 scripts/make_nav.py mkdocs.yml $(CONTRIBUTORS)


####################################################################
install:
	pip install mkdocs
	pip install mkdocs-pdf-export-plugin
	pip install markdown-include
	pip install mkdocs-bootswatch
	pip install python-markdown-math

uninstall:
	pip uninstall -y mkdocs-material
	pip uninstall -y pymdown-extensions
	pip uninstall -y markdown-blockdiag
	pip uninstall -y mkdocs-pdf-export-plugin
