from bmi import bml_caluclator,solti_input,bml_category
def ran():
    print("welcome to the vamsi bmi caluclator")
    weight,height = solti_input()
    bml = bml_caluclator(weight,height)
    category = bml_category(bml)
    print(f"\n Bmi calibration result:")
    print(f"bmi : {bml: 2f}")
    print(f"Category: {category}")
if __name__ == "__main__":
    ran()