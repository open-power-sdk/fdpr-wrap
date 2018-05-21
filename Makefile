# 
# Copyright (C) 2017 IBM Corporation
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

VER_MJR = 0.1
VER_MNR = 1
RELEASE = 8
VER	= $(VER_MJR).$(VER_MNR)
TAR	= fdpr_wrap-$(VER)
DST	= $(DESTDIR)/opt/ibm/fdprpro
RPMBUILD_ROOT=$(PWD)/rpmbuild
DEBBUILD_ROOT=$(PWD)/debian

.PHONY:  default tar install rpm deb mkdirs clean

default: rpm

tar:	mkdirs $(RPMBUILD_ROOT)/SOURCES/$(TAR).tar.gz

$(RPMBUILD_ROOT)/SOURCES/$(TAR).tar.gz:
	mkdir -p $(RPMBUILD_ROOT)/$(TAR)
	cp -a Makefile LICENSE README.md bin $(RPMBUILD_ROOT)/$(TAR)/.
	tar -C $(RPMBUILD_ROOT) -czvf $(RPMBUILD_ROOT)/SOURCES/$(TAR).tar.gz $(TAR)
	rm -rf $(RPMBUILD_ROOT)/$(TAR)

mkdirs:
	mkdir -p $(RPMBUILD_ROOT)/{SOURCES,SRPMS,BUILD,RPMS}

install:
	mkdir -p $(DST)/{bin,share/doc}
	cp -p LICENSE $(DST)/.
	cp -p README.md $(DST)/.
	cp -p bin/fdpr_dl.py $(DST)/bin/.
	cp -p bin/fdpr_instr $(DST)/bin/.
	cp -p bin/fdpr_instr_prof $(DST)/bin/.
	cp -p bin/fdpr_instr_prof_opt $(DST)/bin/.
	cp -p bin/fdpr_instr_prof_jour $(DST)/bin/.
	cp -p bin/fdpr_prof $(DST)/bin/.
	cp -p bin/fdpr_prof_opt $(DST)/bin/.
	cp -p bin/fdpr_prof_jour $(DST)/bin/.
	cp -p bin/fdpr_opt $(DST)/bin/.
	cp -p bin/fdpr_jour $(DST)/bin/.

rpm: mkdirs tar
	sed "s|TOPDIR|$(RPMBUILD_ROOT)|g;s|MAJOR|$(VER_MJR)|g;s|MINOR|$(VER_MNR)|g;s|RELEASE|$(RELEASE)|g" rpm_fdpr_wrap.spec > $(TAR).spec
	rpmbuild -bb --target ppc64le --buildroot $(RPMBUILD_ROOT)/BUILDROOT $(TAR).spec

deb: 
	mkdir -p debian/$(DST)/bin
	cp -p LICENSE debian/$(DST)/LICENSE.fdpr-wrap
	cp -p README.md debian/$(DST)/README.fdpr-wrap.md
	cp -p bin/fdpr_dl.py debian/$(DST)/bin/.
	cp -p bin/fdpr_instr debian/$(DST)/bin/.
	cp -p bin/fdpr_instr_prof debian/$(DST)/bin/.
	cp -p bin/fdpr_instr_prof_opt debian/$(DST)/bin/.
	cp -p bin/fdpr_instr_prof_jour debian/$(DST)/bin/.
	cp -p bin/fdpr_prof debian/$(DST)/bin/.
	cp -p bin/fdpr_prof_opt debian/$(DST)/bin/.
	cp -p bin/fdpr_prof_jour debian/$(DST)/bin/.
	cp -p bin/fdpr_opt debian/$(DST)/bin/.
	cp -p bin/fdpr_jour debian/$(DST)/bin/.
	dpkg-deb --build debian debian

clean:
	rm -rf $(RPMBUILD_ROOT) $(TAR).spec
