Install RetroPie
=======================

**Required Components**

================== ======================
Any Raspberry Pi   1 \* Personal Computer
1 \* Micro SD card 
================== ======================

**Step 1**

Raspberry Pi have developed a graphical SD card writing tool that works
on Mac OS, Ubuntu 18.04 and Windows, and is the easiest option for most
users as it will download the retropie image and install it automatically to the
SD card.

Visit the download page: https://www.raspberrypi.org/software/. Click on
the link for the Raspberry Pi Imager that matches your operating system,
when the download finishes, click it to launch the installer.

.. image:: media/install1.png
    :align: center

**Step 2**

When you launch the installer, your operating system may try to block
you from running it. For example, on Windows I receive the following
message:

If this pops up, click on **More info** and then **Run anyway**, then
follow the instructions to install the Raspberry Pi Imager.

.. image:: media/install2.png
    :align: center

**Step 3**

Insert your SD card into the computer or laptop SD card slot.

**Step 4**

In the Raspberry Pi Imager, select the **Emulation and game OS**.

.. image:: media/install3.png
   :width: 600
   :align: center

Select **RetroPie**.

.. image:: media/install4.png
   :width: 600
   :align: center

Choose the corresponding version according to your Raspberry Pi model.

.. image:: media/install5.png
   :width: 600
   :align: center

**Step 5**

Select the SD card you are using.

.. image:: media/install6.png
   :width: 600
   :align: center

**Step 6**

Press **Ctrl+Shift+X** to open the **Advanced options** page to enable
SSH and configure wifi, these 2 items must be set, the others depend on
your choice . You can choose to always use this image customization
options.

.. image:: media/install7.png
    :width: 600
    :align: center

Then scroll down to complete the wifi configuration and click **SAVE**.

.. note::

    **wifi country** should be set the two-letter `ISO/IEC alpha2
    code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`__ for
    the country in which you are using your Raspberry Pi, please refer to
    the following link: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements

.. image:: media/install8.png
    :width: 600
    :align: center

**Step 7**

Click the **WRITE** button.

.. image:: media/install9.png
    :width: 600
    :align: center

**Step 8**

If your SD card currently has any files on it, you may wish to back up
these files first to prevent you from permanently losing them. If there
is no file to be backed up, click **Yes**.

.. image:: media/install10.png
    :width: 600
    :align: center

**Step 9**

After waiting for a period of time, the following window will appear to
represent the completion of writing.

.. image:: media/install11.png
    :width: 600
    :align: center

After the image is burned, open the config.text file of the SD card to configure the screen resolution.

.. image:: media/install12.png
    :width: 600
    :align: center

Add the following at the end of the file.

.. code-block::

    hdmi_cvt=800 480 60 6
    hdmi_group=2
    hdmi_mode=87
    hdmi_drive=2

.. image:: media/install13.png
    :width: 600
    :align: center

After adding, save the file and you will be able to eject the card reader.