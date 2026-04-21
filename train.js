//TASK-C

// ❓ Shunday function tuzing, u 2ta string parametr ega bolsin,
//hamda agar har ikkala string bir hil harflardan iborat bolsa true
//aks holda false qaytarsin

// ✅ Masalaning yechimi:
function sameLetters(a, b) {
    let sort1 = a.split("").sort().join("");
    let sort2 = b.split("").sort().join("");


    return sort1 === sort2;


}
result = sameLetters("night", "thing");
console.log(result);


// TASK-B

// ❓ Shunday function tuzing, u 1ta string parametrga ega bolsin,
// hamda osha stringda
// qatnashgan raqamlarni sonini bizga return qilsin.

// ✅ Masalaning yechimi:

// function countNumbers(str) {
//     let count = 0;

//     for (let char of str) {
//         if (char >= '0' && char <= '9') {
//             count++;
//         }
//     }

//     return count;
// }

// let result = countNumbers("ajd212efdqfq");
// console.log("result:", result);


// /* TASK-A
// ❓ Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi
// parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
// */

// // ✅ Masalaning yechimi:
// function mevaHarfi(a, b) {
//     let soni = 0;

//     for (let harf of b) {
//         if (harf === a) {
//             soni++
//         }
//     }

//     return soni;
// }

// let result = mevaHarfi("o", "avocado");
// console.log(result)

