KW = 1.0e-14

def sqrt(x):
    return x ** 0.5

def floor(x):
    n = int(x)
    if float(n) > x:
        n = n - 1
    return n

def log10(x):
    y = 0
    while x >= 10.0:
        x = x / 10.0
        y = y + 1
    while x < 1.0:
        x = x * 10.0
        y = y - 1
    lo = 0.0
    hi = 1.0
    for i in range(40):
        mid = (lo + hi) * 0.5
        if 10.0 ** mid <= x:
            lo = mid
        else:
            hi = mid
    return float(y) + (lo + hi) * 0.5

# -- Utilities --

def clr():
    print("\n" * 10)

def hdr(title):
    clr()
    print("-" * 26)
    print(title)
    print("-" * 26)

def pause():
    input("Enter to continue...")

def get_float(prompt):
    try:
        return float(input(prompt))
    except:
        print("Invalid input.")
        pause()
        return None

def quadratic(a, b, c):
    disc = b * b - 4.0 * a * c
    if disc < 0:
        return None
    r1 = (-b + sqrt(disc)) / (2.0 * a)
    r2 = (-b - sqrt(disc)) / (2.0 * a)
    if r1 > 0:
        return r1
    return r2

def fmt(v):
    if v == 0:
        return "0"
    exp = int(floor(log10(abs(v))))
    man = v / (10.0 ** exp)
    return str(round(man, 3)) + "e" + str(exp)

def show_all(ph):
    poh = 14.0 - ph
    h   = 10.0 ** (-ph)
    oh  = 10.0 ** (-poh)
    print("pH  = " + str(round(ph,  4)))
    print("pOH = " + str(round(poh, 4)))
    print("[H+]= " + fmt(h) + " M")
    print("[OH-]=" + fmt(oh) + " M")

# -- Section 1: pH/pOH Basics --

def ph_basics():
    while True:
        hdr("pH/pOH Basics")
        print("1.[H+] -> pH")
        print("2.pH -> [H+]")
        print("3.[OH-] -> pH")
        print("4.pOH -> pH")
        print("5.pH -> pOH/[OH-]")
        print("0.Back")
        ch = input("Choice: ")
        if ch == "0":
            break
        elif ch == "1":
            hdr("pH from [H+]")
            print("pH = -log10([H+])")
            v = get_float("[H+] (mol/L): ")
            if v is None or v <= 0:
                print("Must be > 0")
                pause()
                continue
            ph = -log10(v)
            show_all(ph)
            pause()
        elif ch == "2":
            hdr("[H+] from pH")
            print("[H+] = 10^(-pH)")
            v = get_float("pH: ")
            if v is None or v < 0 or v > 14:
                print("pH must be 0-14")
                pause()
                continue
            show_all(v)
            pause()
        elif ch == "3":
            hdr("pH from [OH-]")
            print("pOH=-log([OH-])")
            print("pH=14-pOH")
            v = get_float("[OH-] (mol/L): ")
            if v is None or v <= 0:
                print("Must be > 0")
                pause()
                continue
            poh = -log10(v)
            ph  = 14.0 - poh
            show_all(ph)
            pause()
        elif ch == "4":
            hdr("pH from pOH")
            print("pH = 14 - pOH")
            v = get_float("pOH: ")
            if v is None or v < 0 or v > 14:
                print("pOH must be 0-14")
                pause()
                continue
            show_all(14.0 - v)
            pause()
        elif ch == "5":
            hdr("pOH/[OH-] from pH")
            print("pOH=14-pH")
            v = get_float("pH: ")
            if v is None or v < 0 or v > 14:
                print("pH must be 0-14")
                pause()
                continue
            show_all(v)
            pause()

# -- Section 2: Strong Acids --

def strong_acids():
    hdr("Strong Acids")
    print("HA -> H+ + A-")
    print("[H+]=C (full diss.)")
    print("Dilute fix if C<1e-7")
    c = get_float("Conc (mol/L): ")
    if c is None or c <= 0:
        print("Invalid.")
        pause()
        return
    if c < 1e-7:
        h = (c + sqrt(c * c + 4.0 * KW)) / 2.0
        print("(water correction)")
    else:
        h = c
    ph = -log10(h)
    show_all(ph)
    pause()

# -- Section 3: Strong Bases --

def strong_bases():
    while True:
        hdr("Strong Bases")
        print("1.Monoprotic (NaOH)")
        print("2.Diprotic (Ca(OH)2)")
        print("0.Back")
        ch = input("Choice: ")
        if ch == "0":
            break
        elif ch == "1" or ch == "2":
            hdr("Strong Bases")
            if ch == "1":
                print("MOH -> M+ + OH-")
                print("[OH-] = C")
            else:
                print("M(OH)2->M2+ + 2OH-")
                print("[OH-] = 2*C")
            c = get_float("Conc (mol/L): ")
            if c is None or c <= 0:
                print("Invalid.")
                pause()
                continue
            if ch == "1":
                oh = c
            else:
                oh = 2.0 * c
            if oh < 1e-7:
                oh = (oh + sqrt(oh * oh + 4.0 * KW)) / 2.0
                print("(water correction)")
            poh = -log10(oh)
            ph  = 14.0 - poh
            show_all(ph)
            pause()

# -- Section 4: Weak Acids --

def weak_acids():
    while True:
        hdr("Weak Acids")
        print("HA <-> H+ + A-")
        print("Ka = x^2/(C-x)")
        print("ICE quadratic")
        print("1.Find pH")
        print("2.% Ionization")
        print("0.Back")
        ch = input("Choice: ")
        if ch == "0":
            break
        elif ch == "1" or ch == "2":
            hdr("Weak Acid Calc")
            print("x^2 + Ka*x - Ka*C=0")
            ka = get_float("Ka: ")
            if ka is None or ka <= 0:
                print("Invalid.")
                pause()
                continue
            c = get_float("Initial [HA] (M): ")
            if c is None or c <= 0:
                print("Invalid.")
                pause()
                continue
            x = quadratic(1.0, ka, -ka * c)
            if x is None or x <= 0:
                print("No solution.")
                pause()
                continue
            ph  = -log10(x)
            pct = (x / c) * 100.0
            show_all(ph)
            if ch == "2":
                print("% ion= " + str(round(pct, 2)) + "%")
            apx = sqrt(ka * c)
            print("Approx [H+]:")
            print(" " + fmt(apx))
            if pct < 5.0:
                print("(<5%: approx valid)")
            else:
                print("(>5%: use quadratic)")
            pause()

# -- Section 5: Weak Bases --

def weak_bases():
    while True:
        hdr("Weak Bases")
        print("B+H2O <-> BH+ + OH-")
        print("Kb = x^2/(C-x)")
        print("1.Find pH")
        print("2.% Ionization")
        print("0.Back")
        ch = input("Choice: ")
        if ch == "0":
            break
        elif ch == "1" or ch == "2":
            hdr("Weak Base Calc")
            print("x^2 + Kb*x - Kb*C=0")
            kb = get_float("Kb: ")
            if kb is None or kb <= 0:
                print("Invalid.")
                pause()
                continue
            c = get_float("Initial [B] (M): ")
            if c is None or c <= 0:
                print("Invalid.")
                pause()
                continue
            x = quadratic(1.0, kb, -kb * c)
            if x is None or x <= 0:
                print("No solution.")
                pause()
                continue
            poh = -log10(x)
            ph  = 14.0 - poh
            pct = (x / c) * 100.0
            show_all(ph)
            if ch == "2":
                print("% ion= " + str(round(pct, 2)) + "%")
            pause()

# -- Section 6: Buffers --

def buffers():
    while True:
        hdr("Buffers")
        print("pH=pKa+log([A-]/[HA])")
        print("1.H-H equation")
        print("2.Add strong acid")
        print("3.Add strong base")
        print("0.Back")
        ch = input("Choice: ")
        if ch == "0":
            break
        elif ch == "1":
            hdr("Henderson-Hasselbalch")
            ka = get_float("Ka: ")
            if ka is None or ka <= 0:
                print("Invalid.")
                pause()
                continue
            a  = get_float("[A-] (M): ")
            ha = get_float("[HA] (M): ")
            if a is None or ha is None or a <= 0 or ha <= 0:
                print("Invalid.")
                pause()
                continue
            pka = -log10(ka)
            ph  = pka + log10(a / ha)
            print("pKa = " + str(round(pka, 4)))
            print("pH  = " + str(round(ph,  4)))
            pause()
        elif ch == "2" or ch == "3":
            if ch == "2":
                hdr("Buffer + Strong Acid")
                print("H+ + A- -> HA")
            else:
                hdr("Buffer + Strong Base")
                print("OH- + HA -> A- + H2O")
            ka    = get_float("Ka: ")
            a_c   = get_float("[A-] initial (M): ")
            ha_c  = get_float("[HA] initial (M): ")
            v_buf = get_float("Buffer vol (L): ")
            c_add = get_float("Strong soln conc(M): ")
            v_add = get_float("Strong soln vol (L): ")
            bad = ka is None or a_c is None or ha_c is None or v_buf is None or c_add is None or v_add is None
            if bad:
                continue
            if ka <= 0 or a_c <= 0 or ha_c <= 0:
                print("All values must be>0")
                pause()
                continue
            if v_buf <= 0 or c_add <= 0 or v_add <= 0:
                print("All values must be>0")
                pause()
                continue
            pka    = -log10(ka)
            mol_a  = a_c  * v_buf
            mol_ha = ha_c * v_buf
            mol_x  = c_add * v_add
            v_tot  = v_buf + v_add
            if ch == "2":
                new_a  = mol_a  - mol_x
                new_ha = mol_ha + mol_x
            else:
                new_a  = mol_a  + mol_x
                new_ha = mol_ha - mol_x
            if new_a <= 0:
                print("Buffer exceeded!")
                excess = -new_a / v_tot
                ph = -log10(excess)
                print("Excess H+:")
                print("pH = " + str(round(ph, 4)))
            elif new_ha <= 0:
                print("Buffer exceeded!")
                excess_oh = -new_ha / v_tot
                ph = 14.0 + log10(excess_oh)
                print("Excess OH-:")
                print("pH = " + str(round(ph, 4)))
            else:
                ph = pka + log10(new_a / new_ha)
                print("New pH = " + str(round(ph, 4)))
            pause()

# -- Section 7: Titrations --

def _sa_sb():
    hdr("Strong A + Strong B")
    print("HCl + NaOH -> NaCl")
    ca = get_float("C_acid (M): ")
    va = get_float("V_acid (L): ")
    cb = get_float("C_base (M): ")
    vb = get_float("V_base added (L): ")
    if ca is None or va is None or cb is None or vb is None:
        return
    if ca <= 0 or va <= 0 or cb <= 0 or vb < 0:
        print("Invalid.")
        pause()
        return
    vep = ca * va / cb
    vt  = va + vb
    print("V_ep=" + str(round(vep * 1000, 2)) + " mL")
    if abs(vb - vep) < 1e-9:
        print("At EP: pH = 7.00")
    elif vb < vep:
        h  = (ca * va - cb * vb) / vt
        ph = -log10(h)
        print("Before EP")
        print("[H+]= " + fmt(h) + " M")
        print("pH  = " + str(round(ph, 4)))
    else:
        oh  = (cb * vb - ca * va) / vt
        poh = -log10(oh)
        ph  = 14.0 - poh
        print("After EP")
        print("[OH-]=" + fmt(oh) + " M")
        print("pH   = " + str(round(ph, 4)))
    pause()

def _wa_sb():
    hdr("Weak A + Strong B")
    print("HA + OH- -> A- + H2O")
    ka = get_float("Ka: ")
    ca = get_float("C_acid (M): ")
    va = get_float("V_acid (L): ")
    cb = get_float("C_base (M): ")
    vb = get_float("V_base added (L): ")
    if ka is None or ca is None or va is None or cb is None or vb is None:
        return
    if ka <= 0 or ca <= 0 or va <= 0 or cb <= 0 or vb < 0:
        print("Invalid.")
        pause()
        return
    pka = -log10(ka)
    vep = ca * va / cb
    vt  = va + vb
    print("V_ep=" + str(round(vep * 1000, 2)) + " mL")
    print("pKa = " + str(round(pka, 4)))
    if vb == 0.0:
        x  = quadratic(1.0, ka, -ka * ca)
        ph = -log10(x)
        print("Weak acid only")
        print("pH = " + str(round(ph, 4)))
    elif abs(vb - vep / 2.0) < 1e-9:
        print("Half-EP: pH = pKa")
        print("pH = " + str(round(pka, 4)))
    elif abs(vb - vep) < 1e-9:
        conc_a  = (ca * va) / vt
        kb_conj = KW / ka
        x       = quadratic(1.0, kb_conj, -kb_conj * conc_a)
        if x is None or x <= 0:
            print("Hydrolysis error")
            pause()
            return
        poh = -log10(x)
        ph  = 14.0 - poh
        print("At EP: A- hydrolysis")
        print("Kb=" + fmt(kb_conj))
        print("pH = " + str(round(ph, 4)))
    elif vb < vep:
        mol_ha = ca * va - cb * vb
        mol_a  = cb * vb
        ph     = pka + log10(mol_a / mol_ha)
        print("Buffer region")
        print("pH = " + str(round(ph, 4)))
    else:
        oh  = (cb * vb - ca * va) / vt
        poh = -log10(oh)
        ph  = 14.0 - poh
        print("After EP: excess OH-")
        print("[OH-]=" + fmt(oh) + " M")
        print("pH   = " + str(round(ph, 4)))
    pause()

def titrations():
    while True:
        hdr("Titrations")
        print("1.Strong A + Strong B")
        print("2.Weak A + Strong B")
        print("0.Back")
        ch = input("Choice: ")
        if ch == "0":
            break
        elif ch == "1":
            _sa_sb()
        elif ch == "2":
            _wa_sb()

# -- Section 8: Ka/Kb Relationships --

def ka_kb_rel():
    while True:
        hdr("Ka/Kb Relations")
        print("Ka * Kb = Kw = 1e-14")
        print("1.Ka -> Kb(conjugate)")
        print("2.Kb -> Ka(conjugate)")
        print("3.Show pKa+pKb=14")
        print("0.Back")
        ch = input("Choice: ")
        if ch == "0":
            break
        elif ch == "1":
            hdr("Ka -> Kb")
            ka = get_float("Ka: ")
            if ka is None or ka <= 0:
                print("Invalid.")
                pause()
                continue
            kb  = KW / ka
            pka = -log10(ka)
            pkb = -log10(kb)
            print("Kb  = " + fmt(kb))
            print("pKa = " + str(round(pka, 4)))
            print("pKb = " + str(round(pkb, 4)))
            print("Sum = " + str(round(pka + pkb, 4)))
            pause()
        elif ch == "2":
            hdr("Kb -> Ka")
            kb = get_float("Kb: ")
            if kb is None or kb <= 0:
                print("Invalid.")
                pause()
                continue
            ka  = KW / kb
            pka = -log10(ka)
            pkb = -log10(kb)
            print("Ka  = " + fmt(ka))
            print("pKa = " + str(round(pka, 4)))
            print("pKb = " + str(round(pkb, 4)))
            print("Sum = " + str(round(pka + pkb, 4)))
            pause()
        elif ch == "3":
            hdr("pKa + pKb = 14")
            print("For conjugate pairs:")
            print("Ka * Kb = Kw = 1e-14")
            print("-log(Ka)-log(Kb)")
            print(" = -log(Kw) = 14")
            print("pKa + pKb = 14.00")
            pause()

# -- Section 9: Polyprotic Acids --

PRESET_NAMES = ["H2CO3", "H2SO3", "H3PO4", "H2S"]
PRESET_KA1   = [4.3e-7,  1.5e-2,  7.5e-3,  1.0e-7]
PRESET_KA2   = [4.7e-11, 6.3e-8,  6.2e-8,  1.0e-19]
PRESET_KA3   = [0.0,     0.0,     4.8e-13, 0.0]

def _diprotic(ka1, ka2, c):
    hdr("Diprotic Calculation")
    print("Step 1: H2A->H+ + HA-")
    x = quadratic(1.0, ka1, -ka1 * c)
    if x is None or x <= 0:
        print("Step 1 error.")
        pause()
        return
    h1 = x
    print("[H+]1 = " + fmt(h1))
    print("Step 2: HA-->H+ + A2-")
    y = quadratic(1.0, h1 + ka2, -ka2 * h1)
    if y is None:
        y = 0.0
    h_tot = h1 + y
    ph    = -log10(h_tot)
    print("[H+]2 = " + fmt(y))
    print("[H+]total=" + fmt(h_tot))
    show_all(ph)
    pause()

def _triprotic(ka1, ka2, ka3, c):
    hdr("Triprotic Calculation")
    print("Step 1: H3A->H+ + H2A-")
    x = quadratic(1.0, ka1, -ka1 * c)
    if x is None or x <= 0:
        print("Step 1 error.")
        pause()
        return
    h1 = x
    print("[H+]1 = " + fmt(h1))
    print("Step 2: H2A-->H+ + HA2-")
    y = quadratic(1.0, h1 + ka2, -ka2 * h1)
    if y is None:
        y = 0.0
    h2 = h1 + y
    print("[H+]2 = " + fmt(y))
    if ka3 > 0:
        print("Step 3: HA2-->H+ + A3-")
        z = quadratic(1.0, h2 + ka3, -ka3 * h2)
        if z is None:
            z = 0.0
        h_tot = h2 + z
        print("[H+]3 = " + fmt(z))
    else:
        h_tot = h2
    ph = -log10(h_tot)
    show_all(ph)
    pause()

def polyprotic():
    while True:
        hdr("Polyprotic Acids")
        print("1.Diprotic (custom)")
        print("2.Triprotic (custom)")
        print("3.Presets")
        print("0.Back")
        ch = input("Choice: ")
        if ch == "0":
            break
        elif ch == "1":
            hdr("Diprotic")
            print("H2A->H++HA->H++A2-")
            ka1 = get_float("Ka1: ")
            ka2 = get_float("Ka2: ")
            c   = get_float("Initial [H2A] (M): ")
            if ka1 is None or ka2 is None or c is None:
                print("Invalid.")
                pause()
                continue
            if ka1 <= 0 or ka2 <= 0 or c <= 0:
                print("Invalid.")
                pause()
                continue
            _diprotic(ka1, ka2, c)
        elif ch == "2":
            hdr("Triprotic")
            print("H3A dissociates 3x")
            ka1 = get_float("Ka1: ")
            ka2 = get_float("Ka2: ")
            ka3 = get_float("Ka3: ")
            c   = get_float("Initial [H3A] (M): ")
            if ka1 is None or ka2 is None or ka3 is None or c is None:
                print("Invalid.")
                pause()
                continue
            if ka1 <= 0 or ka2 <= 0 or ka3 <= 0 or c <= 0:
                print("Invalid.")
                pause()
                continue
            _triprotic(ka1, ka2, ka3, c)
        elif ch == "3":
            hdr("Presets")
            for i in range(len(PRESET_NAMES)):
                print(str(i + 1) + "." + PRESET_NAMES[i])
            print("0.Back")
            ps = input("Choice: ")
            if ps == "0":
                continue
            try:
                idx = int(ps) - 1
            except:
                print("Invalid.")
                pause()
                continue
            if idx < 0 or idx >= len(PRESET_NAMES):
                print("Invalid.")
                pause()
                continue
            hdr(PRESET_NAMES[idx])
            print("Ka1=" + fmt(PRESET_KA1[idx]))
            print("Ka2=" + fmt(PRESET_KA2[idx]))
            if PRESET_KA3[idx] > 0:
                print("Ka3=" + fmt(PRESET_KA3[idx]))
            c = get_float("Concentration (M): ")
            if c is None or c <= 0:
                print("Invalid.")
                pause()
                continue
            if PRESET_KA3[idx] > 0:
                _triprotic(PRESET_KA1[idx], PRESET_KA2[idx], PRESET_KA3[idx], c)
            else:
                _diprotic(PRESET_KA1[idx], PRESET_KA2[idx], c)

# -- Section 10: Reference --

def reference():
    hdr("Ka Reference")
    print("Acid       Ka     pKa")
    print("HF       6.8e-4  3.17")
    print("HAc(AcOH)1.8e-5  4.74")
    print("H2CO3    4.3e-7  6.37")
    print("H2S      1.0e-7  7.00")
    print("HCN      6.2e-10 9.21")
    print("NH4+     5.6e-10 9.25")
    print("HCO3-    4.7e-11 10.33")
    pause()
    hdr("Kb Reference")
    print("Base       Kb     pKb")
    print("CH3NH2   4.4e-4  3.36")
    print("NH3      1.8e-5  4.74")
    print("C6H5NH2  4.3e-10 9.37")
    print("Pyridine 1.7e-9  8.77")
    print("CO3(2-)  2.1e-4  3.68")
    print("HCO3-    2.4e-8  7.62")
    pause()
    hdr("Key Formulas")
    print("pH = -log10([H+])")
    print("pOH= -log10([OH-])")
    print("pH + pOH = 14")
    print("Ka * Kb = 1.0e-14")
    print("Kw=[H+][OH-]=1e-14")
    print("H-H: pH = pKa +")
    print("  log([A-]/[HA])")
    print("V_ep = Ca*Va/Cb")
    pause()
    hdr("AP Exam Tips")
    print("5% rule:")
    print(" if %ion < 5%,")
    print(" approx is valid")
    print("Buffer: pH near pKa")
    print(" (+-1 pH unit)")
    print("At EP(weak A):")
    print(" pH > 7 (basic)")
    print("Half-EP: pH = pKa")
    pause()

# -- Main Menu --

def main():
    while True:
        hdr("AP Chem U8: Acids")
        print("1.pH/pOH Basics")
        print("2.Strong Acids")
        print("3.Strong Bases")
        print("4.Weak Acids")
        print("5.Weak Bases")
        print("6.Buffers")
        print("7.Titrations")
        print("8.Ka/Kb Relations")
        print("9.Polyprotic")
        print("10.Reference")
        print("0.Quit")
        ch = input("Choice: ")
        if ch == "0":
            clr()
            print("Good luck!")
            break
        elif ch == "1":
            ph_basics()
        elif ch == "2":
            strong_acids()
        elif ch == "3":
            strong_bases()
        elif ch == "4":
            weak_acids()
        elif ch == "5":
            weak_bases()
        elif ch == "6":
            buffers()
        elif ch == "7":
            titrations()
        elif ch == "8":
            ka_kb_rel()
        elif ch == "9":
            polyprotic()
        elif ch == "10":
            reference()
        else:
            print("Invalid choice.")
            pause()

main()
