flowchart_v4 = Digraph(format='png', engine='dot')

# Adding nodes for each step
flowchart_v4.node('A', 'Start')
flowchart_v4.node('B', 'Input: Name and Department')
flowchart_v4.node('C', 'Input: Working Hours per Day, Days per Week, Weeks per Month')
flowchart_v4.node('D', 'Calculate Gross Income\nGross Income = Hours x Days x Weeks')
flowchart_v4.node('E', 'Determine Contributions\n(PhilHealth, SSS, Pag-IBIG)')
flowchart_v4.node('F', 'Calculate Total Deduction\nTotal Deduction = SSS + PhilHealth + Pag-IBIG')
flowchart_v4.node('G', 'Calculate Net Income\nNet Income = Gross Income - Total Deduction')
flowchart_v4.node('H', 'Display: Name, Department, Gross Income, Total Deduction, Net Income')
flowchart_v4.node('I', 'End')

# Add edges to connect the flow
flowchart_v4.edge('A', 'B')
flowchart_v4.edge('B', 'C')
flowchart_v4.edge('C', 'D')
flowchart_v4.edge('D', 'E')
flowchart_v4.edge('E', 'F')
flowchart_v4.edge('F', 'G')
flowchart_v4.edge('G', 'H')
flowchart_v4.edge('H', 'I')

# Render and save the flowchart
flowchart_v4_file_path = "/mnt/data/employee_income_computation_flowchart"
flowchart_v4.render(flowchart_v4_file_path)

flowchart_v4_file_path + ".png"