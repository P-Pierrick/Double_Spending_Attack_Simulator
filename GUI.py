# To create a graphical user interface
import tkinter
# To display curves in the GUI
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings
from matplotlib.figure import Figure
# To include the Satoshi's attack function
import SatoshiAttack

root = tkinter.Tk()
# To set the title of the GUI
root.wm_title("Satoshi's Attack")
# To create the figure
fig = Figure(figsize=(5, 4), dpi=100)

# To create a canvas for the figure
canvas = FigureCanvasTkAgg(fig, master=root) 
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# To create a toolbar under the figure
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


# This function allows to update the figure whenever the user changes the Satoshi's attack parameters in the GUI (Graphical User Interface)
def generate_satoshi_attack(event):

    # To clean the figure
    fig.clear()

     # To generate a Satoshi's attack and put the results in the variables
    listRevenueRatioAttacker, listHashrates, list_number_of_cycles_won_per_attack, list_percentage_of_cycles_won_per_attack, list_revenue_per_cycle, list_number_of_blocks_mined_per_cycle, list_time_per_cycle, list_time_per_attack = SatoshiAttack.calculateRevenueRatioForListOfHashrates(z_input_nbConfirmations.get(),
                                                                       v_input_doubleSpendAmount.get(),
                                                                       A_input_maximumAuthorizedDelay.get(),
                                                                       n_input_nbAttacks.get())

    # To display a curve for the attacker
    fig.add_subplot(111).plot(listHashrates, listRevenueRatioAttacker, label='The attacker')

    # To display the curve of the honest miners
    fig.add_subplot(111).plot(listHashrates, listHashrates, label='The honest miners')

    # To add the legend on the fig
    fig.add_subplot(111).legend(loc='best')

    # To display a title for the labels on the figure
    fig.add_subplot(111).set_xlabel('Relative hashrate')
    fig.add_subplot(111).set_ylabel('Revenue ratio')
    # To display a title for the figure
    fig.add_subplot(111).set_title('Double Spending Attack Simulator')

    # To display the figure in the GUI
    canvas.draw()


# The lines below are used to create buttons, these buttons will allow the user to select the value of each parameter

z_input_nbConfirmations = tkinter.Scale(master=root, from_=0, to=10, orient=tkinter.HORIZONTAL, length=200,
                                        label="z : nb of confirmations", command=generate_satoshi_attack)
z_input_nbConfirmations.pack(side=tkinter.LEFT)

n_input_nbAttacks = tkinter.Scale(master=root, from_=1, to=500, orient=tkinter.HORIZONTAL, length=200,
                                  label="n : nb of attacks", command=generate_satoshi_attack)
n_input_nbAttacks.pack(side=tkinter.LEFT)

A_input_maximumAuthorizedDelay = tkinter.Scale(master=root, from_=0, to=20, orient=tkinter.HORIZONTAL, length=200,
                                               label="A : maximum authorized delay", command=generate_satoshi_attack)
A_input_maximumAuthorizedDelay.pack(side=tkinter.LEFT)

v_input_doubleSpendAmount = tkinter.Scale(master=root, from_=0, to=10, orient=tkinter.HORIZONTAL, length=200,
                                          label="v : double spend amount", command=generate_satoshi_attack)
v_input_doubleSpendAmount.pack(side=tkinter.LEFT)

tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is closed with the window manager
