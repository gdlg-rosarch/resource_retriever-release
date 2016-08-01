Name:           ros-indigo-resource-retriever
Version:        1.11.7
Release:        1%{?dist}
Summary:        ROS resource_retriever package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/resource_retriever
Source0:        %{name}-%{version}.tar.gz

Requires:       curl
Requires:       libcurl-devel
Requires:       python-urlgrabber
Requires:       ros-indigo-rosconsole
Requires:       ros-indigo-roslib
BuildRequires:  curl
BuildRequires:  libcurl-devel
BuildRequires:  ros-indigo-catkin >= 0.5.68
BuildRequires:  ros-indigo-rosconsole
BuildRequires:  ros-indigo-roslib

%description
This package retrieves data from url-format files such as http://, ftp://,
package:// file://, etc., and loads the data into memory. The package:// url for
ros packages is translated into a local file:// url. The resourse retriever was
initially designed to load mesh files into memory, but it can be used for any
type of data. The resource retriever is based on the the libcurl library.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Aug 01 2016 Ioan Sucan <isucan@gmail.com> - 1.11.7-1
- Autogenerated by Bloom

* Mon Aug 01 2016 Ioan Sucan <isucan@gmail.com> - 1.11.7-0
- Autogenerated by Bloom

* Tue Apr 21 2015 Ioan Sucan <isucan@gmail.com> - 1.11.6-0
- Autogenerated by Bloom

