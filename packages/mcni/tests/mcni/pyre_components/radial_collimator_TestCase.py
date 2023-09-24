import numpy as np
import pyre.inventory as pinv
from pyre.applications.Script import Script
from mcni.pyre_components.RadialCollimator import RadialCollimator

def check_parameters(app_name, parameter_set):
    class TestApp(Script):

        class Inventory(Script.Inventory):
            rc = pinv.facility(name='rc', default=RadialCollimator('rc'))

        def main(self):
            rc = self.inventory.rc
            engine = rc.engine
            for k, expected_value in parameter_set.items():
                value = getattr(engine, k)
                if hasattr(expected_value, "__iter__"):
                    assert np.allclose(value, expected_value), f"{value} != {expected_value}"
                else:
                    assert value == expected_value, f"{value} != {expected_value}"
    app = TestApp(app_name)
    app.run()
    return

def main():
    check_parameters(
        "radial_collimator_test_app_theta_list",
        dict(
            theta_list = np.array([1,2,4,7])*(np.pi/180),
            theta_min = np.pi/180,
            theta_max = 7*np.pi/180,
        )
    )
    check_parameters(
        "radial_collimator_test_app_evenly_spaced_theta",
        dict(
            theta_min = 0.,
            theta_max = np.pi,
            dtheta = np.pi/12,
        )
    )


if __name__ == '__main__': main()
