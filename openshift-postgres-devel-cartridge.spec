%global cartridgedir %{_libexecdir}/openshift/cartridges/crunchypg-devel-cart

Summary:       Provides Crunchy Postgres Developer tools support
Name:          openshift-postgres-devel-cartridge
Version:       1.0.3
Release:       1%{?dist}
Group:         Development/Languages
License:       ASL 2.0
URL:           http://www.openshift.com
Source0:       file:///./%{name}-%{version}.tar.gz
Requires:      lsof
Requires:      bc
Requires:      /bin/sh

%description
provides crunchy postresql developer tools

%prep
%setup -q

%build
%__rm %{name}.spec

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}

%post

%{_sbindir}/oo-admin-cartridge --action install --source %{cartridgedir}


%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%{cartridgedir}
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/LICENSE

%changelog
* Tue May 13 2014 jeff mccormick <jeffmc04@gmail.com> 1.0.3-1
- 

* Tue May 13 2014 jeff mccormick <jeffmc04@gmail.com> 1.0.2-1
- new package built with tito

* Tue May 13 2014 jeff mccormick <jeffmc04@gmail.com> 1.0.1-1
- new package built with tito



