Name:           ros-indigo-constrained-ik
Version:        0.1.1
Release:        0%{?dist}
Summary:        ROS constrained_ik package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://ros.org/wiki/constrained_ik
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-indigo-cmake-modules
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-eigen-conversions
Requires:       ros-indigo-industrial-collision-detection
Requires:       ros-indigo-kdl-parser
Requires:       ros-indigo-moveit-core
Requires:       ros-indigo-moveit-ros-planning
Requires:       ros-indigo-orocos-kdl
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-tf-conversions
Requires:       ros-indigo-urdf
BuildRequires:  boost-devel
BuildRequires:  gtest-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-eigen-conversions
BuildRequires:  ros-indigo-industrial-collision-detection
BuildRequires:  ros-indigo-kdl-parser
BuildRequires:  ros-indigo-moveit-core
BuildRequires:  ros-indigo-moveit-ros-planning
BuildRequires:  ros-indigo-orocos-kdl
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-tf-conversions
BuildRequires:  ros-indigo-urdf

%description
Constraint-based IK solver. Good for high-DOF robots or underconstrained tasks.

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
* Fri Mar 24 2017 Jeremy Zoss, SwRI <jzoss@swri.org> - 0.1.1-0
- Autogenerated by Bloom

* Mon Mar 20 2017 Jeremy Zoss, SwRI <jzoss@swri.org> - 0.1.0-0
- Autogenerated by Bloom

