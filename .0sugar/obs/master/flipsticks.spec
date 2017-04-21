# This file was generated from Zero Sugar spec file and will be overriden
# during the next uploading session to home:alsrooot:Sugar:Contrib OBS project.
# Sources with spec file might be found on http://packages.sugarlabs.org/flipsticks.
# See http://wiki.sugarlabs.org/go/Activity_Team/Zero_Sugar for details.

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

Name: sugar-flipsticks
Version: 6
Release: 1
Group: Development/Tools/Other
Summary: Using keyframes, program a stick figure to twist and dance
License: GPLv2+
Url: http://wiki.sugarlabs.org/go/Activities/Flip_Sticks

Source: flipsticks-6.tar.gz

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

BuildRequires: 0distro
Provides: sugar-flipsticks-devel = %{version}-%{release}

%description
Flipsticks is a keyframe animation activity that lets you pose
and program a stick figure to walk, run, rotate, twist, tumble and
dance. You can save your animations to the journal and will soon be
able to share them via the mesh. Flipsticks can be used to explore
concepts in geometry, computer programming and animation; it helps
develop spatial and analytical thinking skills.

%prep
%setup -n flipsticks-6

%build
/usr/bin/0distro-build --verbose configure %{buildroot}
/usr/bin/0distro-build --verbose make %{buildroot}

%install
rm -rf %{buildroot}

/usr/bin/0distro-build --verbose --clean-up install %{buildroot} rpm

%clean
rm -rf %{buildroot}

%files -f sugar-flipsticks.install

%changelog
