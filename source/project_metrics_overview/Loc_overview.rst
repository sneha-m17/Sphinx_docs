
LOC Chart Overview
====================

Pie Chart Category
^^^^^^^^^^^^^^^^^^^^
.. grid:: 3
   :gutter: 2

   .. card:: 📝 **Total TODO LOC**
      :class-card: sd-shadow-xs sd-rounded sd-bg-white sd-border sd-padding-sm sd-text-sm
      :link: #todo-loc

      - Shows percentage and total count of **lines of code pending** for processing.

   .. card:: 🔍 **Total Analyzed LOC**
      :class-card: sd-shadow-xs sd-rounded sd-bg-white sd-border sd-padding-sm sd-text-sm
      :link: #analyzed-loc

      - Displays percentage and total count of **analyzed lines of code**.

   .. card:: 🔁 **Total Converted LOC**
      :class-card: sd-shadow-xs sd-rounded sd-bg-white sd-border sd-padding-sm sd-text-sm
      :link: #converted-loc

      - Percentage and count of **converted LOC** files shown here.

.. grid:: 3
   :gutter: 2

   .. card:: ✅ **Total Validated LOC**
      :class-card: sd-shadow-xs sd-rounded sd-bg-white sd-border sd-padding-sm sd-text-sm
      :link: #validated-loc

      - Displays percentage and total **validated LOC**.

   .. card:: 🔄 **Total Reconciled LOC**
      :class-card: sd-shadow-xs sd-rounded sd-bg-white sd-border sd-padding-sm sd-text-sm
      :link: #reconciled-loc

      - Indicates reconciled LOC with **total and percentage**.

   .. card:: ❌ **Total Error LOC**
      :class-card: sd-shadow-xs sd-rounded sd-bg-white sd-border sd-padding-sm sd-text-sm
      :link: #error-loc

      - Shows proportion and count of **lines of code with errors**.


Bar Chart Category
^^^^^^^^^^^^^^^^^^^^^^

The Bar Chart displays key project-level metrics related to lines of code and errors, helping users assess the overall code volume, code complexity, and error count.

.. grid:: 3
   :gutter: 2

   .. card:: 📄 **Total Lines in Files**
      :class-card: sd-shadow-xs sd-rounded sd-bg-light sd-border-muted sd-padding-sm sd-text-sm
      :link: #total-lines

      - Total number of lines across all files in the project.
      - Gives an overview of the **data volume** handled.

   .. card:: 💻 **Total Lines of Code**
      :class-card: sd-shadow-xs sd-rounded sd-bg-light sd-border-muted sd-padding-sm sd-text-sm
      :link: #total-loc

      - Indicates total **lines of actual code (LOC)** across files.
      - Helps measure **codebase size and complexity**.

   .. card:: ⚠️ **Total Errors**
      :class-card: sd-shadow-xs sd-rounded sd-bg-light sd-border-muted sd-padding-sm sd-text-sm
      :link: #total-errors

      - Shows the number of **errors detected** in the LOC.
      - Summarizes issues to be addressed for project health.


Line Chart Category
^^^^^^^^^^^^^^^^^^^^^

Displays trends in lines of code (LOC) over time across various file statuses. Users can interact with the chart and explore different data views and tools.

.. grid:: 2
   :gutter: 2

   .. card:: 🧭 **Interactive Menu**
      :class-card: sd-shadow-xs sd-rounded sd-bg-white sd-border sd-padding-sm sd-text-sm
      :link: #line-menu

      - **Download PNG**: Save the chart as a raster image.
      - **Download CSV**: Export underlying chart data for analysis.
      - **Download SVG**: Save as scalable vector graphics.

   .. card:: 🔍 **Zoom & Pan Tools**
      :class-card: sd-shadow-xs sd-rounded sd-bg-white sd-border sd-padding-sm sd-text-sm
      :link: #line-tools

      - **Panning**: Drag to move across the chart.
      - **Zoom In/Out**: Focus or expand the view.
      - **Zoom Reset**: Restore default zoom level.

.. grid:: 3
   :gutter: 2

   .. card:: 🟢 **TODO LOC**
      :class-card: sd-shadow-xs sd-rounded sd-bg-white sd-border sd-padding-sm sd-text-sm
      :link: #line-todo

      - Lines of code pending for processing.

   .. card:: 🟡 **Analyzed LOC**
      :class-card: sd-shadow-xs sd-rounded sd-bg-white sd-border sd-padding-sm sd-text-sm
      :link: #line-analyzed

      - LOC from files that have been analyzed.

   .. card:: 🔵 **Converted LOC**
      :class-card: sd-shadow-xs sd-rounded sd-bg-white sd-border sd-padding-sm sd-text-sm
      :link: #line-converted

      - LOC from files that have been converted.

.. grid:: 3
   :gutter: 2

   .. card:: 🟣 **Validated LOC**
      :class-card: sd-shadow-xs sd-rounded sd-bg-white sd-border sd-padding-sm sd-text-sm
      :link: #line-validated

      - LOC from files that have been validated.

   .. card:: 🟠 **Reconciled LOC**
      :class-card: sd-shadow-xs sd-rounded sd-bg-white sd-border sd-padding-sm sd-text-sm
      :link: #line-reconciled

      - LOC from files that have been reconciled.

   .. card:: 🔴 **Error LOC**
      :class-card: sd-shadow-xs sd-rounded sd-bg-white sd-border sd-padding-sm sd-text-sm
      :link: #line-error

      - LOC from files with processing errors.
