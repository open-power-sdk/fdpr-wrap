VER_MJR = 0.1.0
VER_MNR = 1
VER	= $(VER_MJR).$(VER_MNR)
RPM_VER	= $(VER_MJR)-$(VER_MNR)
SRC	= .
PKG	= fdpr_wrap-$(RPM_VER)
TAR	= fdpr_wrap-$(VER)
TOP	= /tmp/hrl
DST	= $(TOP)/opt/ibm/fdprpro
OWNER	= -o bin -g bin
# for SuSe
RPMDIR	= /usr/src/packages/RPMS/ppc64
RPMDIR	=  ~/rpmbuild/RPMS/ppc64le
# for redhat or fedora
#RPMDIR	= /usr/src/redhat/RPMS/ppc64le
#FDPRTOOLS	= should be defined by the user

.PHONY:  default tar install package

default: package

mkdirs:
	sudo rm -rf $(TOP) 
	sudo mkdir $(TOP) $(TOP)/bin $(TOP)/lib $(TOP)/share $(TOP)/share/doc
	sudo mkdir $(TOP)/opt $(TOP)/opt/ibm # DST ancestors
	sudo mkdir $(DST) $(DST)/bin $(DST)/lib $(DST)/share $(DST)/share/doc

install:
	sudo install $(OWNER) -m 644 -D $(SRC)/share/doc/license_files-wrapper.zip    $(DST)/share/doc/license_files-wrapper.zip
	sudo install $(OWNER) -m 644 -D $(SRC)/share/doc/README-WRAPPER.txt $(DST)/share/doc/README-WRAPPER.txt
	sudo install $(OWNER) -m 644 -D $(SRC)/share/doc/COPYRIGHT-WRAPPER    $(DST)/share/doc/COPYRIGHT-WRAPPER
	sudo install $(OWNER) -m 755 -D $(SRC)/bin/fdpr_dl.py		      $(DST)/bin/fdpr_dl.py
	sudo install $(OWNER) -m 755 -D $(SRC)/bin/fdpr_instr		      $(DST)/bin/fdpr_instr
	sudo install $(OWNER) -m 755 -D $(SRC)/bin/fdpr_instr_prof	      $(DST)/bin/fdpr_instr_prof
	sudo install $(OWNER) -m 755 -D $(SRC)/bin/fdpr_instr_prof_opt	      $(DST)/bin/fdpr_instr_prof_opt
	sudo install $(OWNER) -m 755 -D $(SRC)/bin/fdpr_instr_prof_jour	      $(DST)/bin/fdpr_instr_prof_jour
	sudo install $(OWNER) -m 755 -D $(SRC)/bin/fdpr_prof		      $(DST)/bin/fdpr_prof
	sudo install $(OWNER) -m 755 -D $(SRC)/bin/fdpr_prof_opt	      $(DST)/bin/fdpr_prof_opt
	sudo install $(OWNER) -m 755 -D $(SRC)/bin/fdpr_prof_jour	      $(DST)/bin/fdpr_prof_jour
	sudo install $(OWNER) -m 755 -D $(SRC)/bin/fdpr_opt		      $(DST)/bin/fdpr_opt
	sudo install $(OWNER) -m 755 -D $(SRC)/bin/fdpr_jour		      $(DST)/bin/fdpr_jour

package: mkdirs install
	perl -ape "s/: w.x.y/: $(VER_MJR)/; s/: z/: $(VER_MNR)/;" rpm_fdpr_wrap.spec >  $(PKG).spec
	tar -czvf fdpr_wrap.tgz $(TOP)/ 
	rpmbuild -bb --target ppc64le --buildroot $(TOP) $(PKG).spec
	cp -p $(RPMDIR)/fdpr_wrap-$(RPM_VER).ppc64le.rpm $(PKG).ppc64le.rpm
	chown $(USER):$(USER) $(PKG).ppc64le.rpm $(PKG).spec
