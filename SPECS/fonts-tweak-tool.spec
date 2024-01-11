Name: fonts-tweak-tool
Version: 0.4.5
Release: 3%{?dist}
Summary: Tool for customizing fonts per language

License: LGPLv3+
URL: https://bitbucket.org/tagoh/%{name}/
Source0: https://bitbucket.org/tagoh/%{name}/downloads/%{name}-%{version}.tar.bz2
Patch0:	%{name}-drop-pyxdg.patch

BuildRequires: desktop-file-utils
BuildRequires: intltool
BuildRequires: python3-devel
BuildRequires: gobject-introspection-devel glib2-devel
Requires: libeasyfc-gobject >= 0.14.0
Requires: python3-gobject
Requires: gtk3
Requires: hicolor-icon-theme

%description
fonts-tweak-tool is a GUI tool for customizing fonts per language on desktops
using fontconfig.

%prep
%autosetup -p1

%configure --disable-static PYTHON=%{__python3}

%build
make %{?_smp_mflags}

%install
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications fonts-tweak-tool.desktop
make install DESTDIR=${RPM_BUILD_ROOT} INSTALL="/usr/bin/install -p"

rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.{la,so}
rm -f $RPM_BUILD_ROOT%{_datadir}/gir-*/FontsTweak-*.gir

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%doc README AUTHORS NEWS
%license COPYING
%{_bindir}/%{name}
%{python3_sitearch}/fontstweak
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_libdir}/libfontstweak-resources.so.0*
%{_libdir}/girepository-*/FontsTweak-*.typelib

%changelog
* Thu Jul 19 2018 Akira TAGOH <tagoh@redhat.com> - 0.4.5-3
- Drop dep of pyxdg.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Akira TAGOH <tagoh@redhat.com> - 0.4.5-1
- New upstream release.
- Use %%{__python3} macro instead of the hardcoded python3 name.

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-5
- Rebuilt for Python 3.7

* Fri Jun 29 2018 Akira TAGOH <tagoh@redhat.com> - 0.4.3-4
- Use ldconfig rpm macro.

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-3
- Rebuilt for Python 3.7

* Fri Jun 15 2018 Akira TAGOH <tagoh@redhat.com> - 0.4.3-2
- R: python3-gobject instead of pygobject3.

* Thu May 24 2018 Akira TAGOH <tagoh@redhat.com> - 0.4.3-1
- New upstream release.
- Fix invalid plural forms expression (#1568991)

* Tue Feb 20 2018 Akira TAGOH <tagoh@redhat.com> - 0.4.2-1
- New upstream release.
- Fix the version deps check.

* Fri Feb 16 2018 Akira TAGOH <tagoh@redhat.com> - 0.4.1-1
- New upstream release.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-12
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-11
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Apr 11 2016 Akira TAGOH <tagoh@redhat.com> - 0.3.2-10
- Update shebang for python3.

* Wed Apr 06 2016 Parag Nemade <pnemade AT redhat DOT com>
- move to python3 as default support
- add %%license
- Remove group tag as its obsolete now

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.3.2-7
- Add an AppData file for the software center

* Thu Sep  4 2014 Akira TAGOH <tagoh@redhat.com> - 0.3.2-6
- Fix PyGTKDeprecationWarnings. (#1136177)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.3.2-4
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb  7 2014 Akira TAGOH <tagoh@redhat.com> - 0.3.2-2
- Fix the installation path for python scripts (#1062560)

* Wed Jul 31 2013 Akira TAGOH <tagoh@redhat.com> - 0.3.2-1
- New upstream release.

* Thu Apr 18 2013 Akira TAGOH <tagoh@redhat.com> - 0.3.1-1
- New upstream release.
  - Fix a crash. (#952983)

* Fri Mar 29 2013 Akira TAGOH <tagoh@redhat.com> - 0.3.0-1
- New upstream release.

* Tue Feb 26 2013 Akira TAGOH <tagoh@redhat.com> - 0.2.0-1
- New upstream release.
  - Improve UI (#909769)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 22 2013 Akira TAGOH <tagoh@redhat.com> - 0.1.5-1
- New upstream release.
  - Updated translations (#816378)

* Tue Dec 18 2012 Akira TAGOH <tagoh@redhat.com> - 0.1.4-1
- New upstream release.
  - Fix file writing issue when the classification filter is turned off.
    (#886330)

* Sat Nov 24 2012 Akira TAGOH <tagoh@redhat.com> - 0.1.2-1
- New upstream release
  - Fix broken icons issue on non-GNOME desktops (#879140)

* Wed Nov 21 2012 Akira TAGOH <tagoh@redhat.com> - 0.1.1-3
- Fix a typo

* Wed Nov 21 2012 Akira TAGOH <tagoh@redhat.com> - 0.1.1-2
- clean up and improve the spec file.

* Mon Oct 22 2012 Akira TAGOH <tagoh@redhat.com> - 0.1.1-1
- New upstream release.
  - Drop the unnecessary warnings (#859455)

* Wed Sep 19 2012 Akira TAGOH <tagoh@redhat.com> - 0.1.0-1
- New upstream release.

* Mon Aug 06 2012 James Ni <kent.neo@gmail.com> - 0.0.8-1
- Apply pull request from tagoh

* Tue Jul 24 2012 James Ni <kent.neo@gmail.com> - 0.0.7-1
- Fixed rhbz#838871, Apply button is always clickable
- Fixed rhbz#838854, existing settings in .i18n isn't reflected to initial value
- Fixed rhbz#838865, Unable to remove language in GTK Language Order tab
- Fixed rhbz#838850 - empty language added to .i18n

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 27 2012 James Ni <jni@redhat.com> - 0.0.6-1
- Implement pango_language feature and bug fix

* Tue Mar 20 2012 James Ni <jni@redhat.com> - 0.0.5-1
- Fix issue of 'UnicodeWarning: Unicode equal comparison failed'

* Mon Mar 19 2012 James Ni <jni@redhat.com> - 0.0.4-1
- Bug fix and feature enhancement

* Thu Feb 23 2012 James Ni <jni@redhat.com> - 0.0.3-1
- Fix the issue of spec file

* Fri Feb 17 2012 James Ni <jni@redhat.com> - 0.0.2-3
- Fix the issue of spec file

* Wed Feb 08 2012 James Ni <jni@redhat.com> - 0.0.2-2
- Fix the issue of spec file

* Tue Feb 07 2012 James Ni <jni@redhat.com> - 0.0.2-1
- Update the licenses file and modify the spec file

* Mon Feb 06 2012 James Ni <jni@redhat.com> - 0.0.1-1
- initial package
