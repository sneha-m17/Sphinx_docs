===============
Project Level
===============

To examine data flows within the process, navigate to the **Project Level** section under **Data Lineage**.
Upon selecting a file, the system displays the flow of data between projects. Double-clicking on a node provides a detailed view of the specific flow associated with that node.

.. image:: _static/Project_level/projectlevel_page.png
   :width: 900px
   :alt: Project Level page
   :align: center
   :class: soft-edge

Each block includes the following functionality:

.. image:: _static/Project_level/Block.png
   :width: 300px
   :alt: Block
   :align: center
   :class: soft-edge

**1. Input and Output:** Shows the input and output tables linked to the block, including details such as the file name, block ID, and block label. Additionally, a **View** option is available, allowing users to access the block's code. This includes a summary, the actual code, relevant metrics, a docstring, and a code similarity analysis.

**2. Data Match:** Displays the datamatch table, providing a report on matched and mismatched columns between the source and target tables.

Features
""""""""

The Main features of Project Level Data Lineage includes

1. Merlin AI
2. File Layout
3. Regenerate Graph
4. Save Graph
5. Reset Graph 

.. image:: _static/Project_level/Key_options.png
   :width: 300px
   :alt: key options
   :align: center
   :class: soft-edge

Merlin AI
^^^^^^^^^^

Project Level MerlinAI is an advanced AI assistant designed to address user queries and provide relevant information based on contextual needs. It offers both **global** and **project-specific** support.

- When a node is clicked, **MerlinAI** opens, displaying the **Overview** and **Usage** sections. The **Lineage Table** is provided, containing details such as upstream and downstream, dataset, file name, block ID, and dependency type. Clicking on **actions** within the table reveals the **block code** of the selected node.

.. image:: _static/Project_level/MerlinAI.png
   :width: 250px
   :alt: Merlin AI 
   :align: center
   :class: soft-edge

- Additionally, users can directly access the **block code** within **MerlinAI** for a specific node, along with detailed information about the **node, source dataset, and target dataset**.

.. image:: _static/Project_level/Overview&usage.png
   :width: 900px
   :alt: Overview and Usage
   :align: center
   :class: soft-edge

File Layout 
^^^^^^^^^^^^

Users can customize the layout based on the Algorithm, Direction, and Spacing settings.

**1. Algorithm -** 
Users can choose from three algorithms to calculate the element layout
 
- Dagre
- D3 Hierarchy
- ELK

.. image:: _static/Project_level/File_layout.png
   :width: 400px
   :alt: File Layout Screenshot
   :align: center
   :class: soft-edge

**2. Direction -**
Users can define the flow direction of the layout. They are,

- TB: Top to Bottom
- LR: Left to Right
- BT: Bottom to Top
- RL: Right to Left

**3. Spacing -**
Users can adjust the spacing between elements, using both horizontal and vertical spacing.

Regenerate Graph
^^^^^^^^^^^^^^^^^

The purpose of **Regenerate Graph** option is to restore the Project lineage to its original state.

A confirmation prompt will appear to safeguard against unintentional changes.

.. image:: _static/Project_level/Regenerate_graph.png
   :width: 900px
   :alt: Regenerate Graph Confirmation Screenshot
   :align: center
   :class: soft-edge

Save Graph
^^^^^^^^^^^

This option ensures that all your modifications are preserved.

Reset Graph
^^^^^^^^^^^^

This option reverts the graph to its original state unless you have explicitly saved your changes. Any modifications made will be preserved.

Settings
"""""""""
This option is placed at the left side bottom of the screen.

.. image:: _static/Project_level/Settings.gif
   :width: 900px
   :alt: Settings Option Screenshot
   :align: center
   :class: soft-edge

Project Data workflow Settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This manages block visibility and relationships in the workflow.

.. image:: _static/Project_level/Data_workflow_settings.png
   :width: 500px
   :alt: Project Data workflow Settings Screenshot
   :align: center
   :class: soft-edge

**Edge Settings** manages the display of connections and relationships between blocks.
 - **Show Edge Relations:** display the block names like Datastep, Proc Import, marco on the edges between blocks in the workflow. This helps visualize the relationships and interactions between blocks.

.. image:: _static/Project_level/Edge_relations.png
   :width: 500px
   :alt: Show edge Relations Screenshot
   :align: center
   :class: soft-edge

- **Enable Animations:** It makes transitions between workflow states more fluid and visually enagaging.

.. image:: _static/Project_level/Animation_settings.png
   :width: 500px
   :alt: Show edge Relations Screenshot
   :align: center
   :class: soft-edge

Cumulative Node
""""""""""""""""

- Within the **Project Level** settings, the **Threshold** value is set to **10** by default. 
- If the number of blocks in a project exceeds **10**, cumulative nodes are displayed. 
- The **start** and **end** blocks remain visible, with the **Lineage** highlighted.

.. image:: _static/Project_level/Cumulative_node.png
   :width: 900px
   :alt: Cumulative Node Screenshot
   :align: center
   :class: soft-edge

- Clicking on the **Lineage** between nodes reveals the cumulative nodes within it. 
- Additionally, the **Threshold** value can be adjusted from the **Settings** tab in the project-level panel.
