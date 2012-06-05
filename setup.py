

from distutils.core import setup

setup(name="gratia-gold",
      version="0.2",
      author="Yaling Zheng",
      author_email="yaling.zheng@gmail.com",
      url="https://github.com/YalingZheng/gratia-gold",
      description="Probe for synchronizing Gratia and GOLD",
      package_dir={"": "src"},
      packages=["gratia_gold"],

      data_files=[("/etc/cron.d", ["config/gratia-gold.cron"]),
            ("/etc/", ["config/gratia-gold.cfg"]),
            ("/etc/logrotate.d", ["config/gratia-gold.logrotate"]),
            ("/usr/bin", ["src/gratia-gold"]),
          ],

     )

