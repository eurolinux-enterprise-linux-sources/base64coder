%global long_ver  2010-12-19

Name:           base64coder
Version:        20101219
Release:        9%{?dist}
Summary:        Fast and compact Base64 encoder/decoder Java library
License:        EPL or LGPLv2+ or GPLv2+ or ASL 2.0+ or BSD
BuildArch:      noarch
URL:            http://www.source-code.biz/%{name}/java/
Source0:        http://repo2.maven.org/maven2/biz/source_code/%{name}/%{long_ver}/%{name}-%{long_ver}-distribution.zip

BuildRequires:  maven-local
BuildRequires:  mvn(org.sonatype.oss:oss-parent)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

%description
Base64Coder is a fast and compact Base64 encoder/decoder class.

There is no Base64 encoder/decoder in the standard Java SDK class
library.  The undocumented classes sun.misc.BASE64Encoder and
sun.misc.BASE64Decoder should not be used.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package contains %{summary}.

%prep
%setup -q -n %{name}-%{long_ver}
sed -i 's/\r//g' README.txt CHANGES.txt
%mvn_file : %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.txt CHANGES.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 20101219-9
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Fri Jun 14 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 20101219-8
- Update to current packaging guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101219-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 20101219-6
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101219-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 21 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 20101219-4
- Add maven plugins to BuildRequires

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101219-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 07 2011 Jaromir Capik <jcapik@redhat.com> - 20101219-2
- Java suffix removed from the package name and put in the summary instead
- Version string added in the source URL (no need for manual renaming)
- POM file added in the source package -> Source1 removed (no need for copying)
- Removal of the target directory removed (not present anymore)

* Mon May 30 2011 Jaromir Capik <jcapik@redhat.com> - 20101219-1
- Initial version of the package
