import os

from tests.testing import _test_tf_template

root = os.path.dirname(os.path.abspath(__file__))
tf_plan_path = os.path.join(root, "main.tfplan")

tpl = {
    "ROSTemplateFormatVersion": "2015-09-01",
    "Resources": {
        "alicloud_ens_disk.default": {
            "Type": "ALIYUN::ENS::Disk",
            "Properties": {
                "Category": "cloud_ssd",
                "EnsRegionId": "cn-chongqing-11",
                "Size": 20,
            },
        }
    },
}


def test_template():
    t = _test_tf_template(root, tf_plan_path)
    assert t == tpl
