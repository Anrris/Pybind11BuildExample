
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/eigen.h>
#include <pybind11/stl.h>
#include <pybind11/complex.h>
#include <pybind11/functional.h>
#include <pybind11/chrono.h>
namespace py = pybind11;

#include <iostream>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <fstream>
#include <cstdlib>

#include <Eigen/Dense>
#include <boost/geometry.hpp>
//#include "src/aric.h"

void run_test(){
    using namespace std;
    cout << "DDD" << endl;
}

PYBIND11_MODULE(setup_test, m) {

    m.def("run_test", &run_test);

}
