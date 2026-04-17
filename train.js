/* TASK-A
❓ Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi
parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
*/

// ✅ Masalaning yechimi:
function mevaHarfi(a, b) {
    let soni = 0;

    for (let harf of b) {
        if (harf === a) {
            soni++
        }
    }

    return soni;
}

let result = mevaHarfi("o", "avocado");
console.log(result)
