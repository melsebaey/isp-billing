# 📡 ISP Billing

<div align="center">

![Status](https://img.shields.io/badge/status-active-success.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![Language](https://img.shields.io/badge/language-AR%20%7C%20EN-orange.svg)

**ISP Billing Management System / نظام إدارة فواتير مزود خدمة الإنترنت**

Bilingual Interface (Arabic / English) · Dark Theme · Real-time Financial Reports

</div>

---

## 📑 Table of Contents / المحتويات

- [Overview / نظرة عامة](#-overview--نظرة-عامة)
- [Features / المميزات](#-features--المميزات)
- [Getting Started / التشغيل](#-getting-started--التشغيل)
- [Accessing the Application / الوصول إلى التطبيق](#-accessing-the-application--الوصول-إلى-التطبيق)
- [Default Login Credentials / بيانات الدخول الافتراضية](#-default-login-credentials--بيانات-الدخول-الافتراضية)
- [Network Access / الوصول عبر الشبكة](#-network-access--الوصول-عبر-الشبكة)
- [Application Modules / وحدات التطبيق](#-application-modules--وحدات-التطبيق)
- [Requirements / المتطلبات](#-requirements--المتطلبات)
- [Troubleshooting / استكشاف الأخطاء](#-troubleshooting--استكشاف-الأخطاء)
- [Support / الدعم](#-support--الدعم)

---

## 🔭 Overview / نظرة عامة

### English

The **ISP Billing** application is a comprehensive management system for Internet Service Providers. It enables you to manage customers, packages, accounts, invoices, payments, expenses, and technical support tickets, with powerful real-time financial reports. The interface supports both **Arabic and English** with a modern dark theme.

### العربية

تطبيق **ISP Billing** هو نظام إدارة متكامل لمزوّدي خدمة الإنترنت. يتيح لك إدارة العملاء والباقات والحسابات والفواتير والمدفوعات والمصروفات وتذاكر الدعم الفني، مع تقارير مالية قوية آنية. يدعم الواجهة **العربية والإنجليزية** بتصميم داكن عصري، .

---

## ✨ Features / المميزات

### English

- 🌐 **Bilingual Interface** — Full support for Arabic (RTL) and English (LTR)
- 🌙 **Modern Dark Theme** — Comfortable viewing experience, day or night
- 📊 **Comprehensive Financial Reports** — Subscription income, other income, total income, expenses, net profit, invoices count
- 📋 **Debtors Report** — Track outstanding payments and customer debts
- 📅 **Date Range Filtering** — Monthly reports or custom date ranges
- 🖨️ **Export & Print** — One-click PDF print and Excel export
- 💵 **Multi-Payment Methods** — Cash and Bank Transfer tracking
- 👥 **Role-Based Access** — Administrator and Collector accounts with different permissions
- 📱 **Network Access** — Use from any device on the same local network

### العربية

- 🌐 **واجهة ثنائية اللغة** — دعم كامل للعربية (RTL) والإنجليزية (LTR)
- 🌙 **تصميم داكن عصري** — تجربة مشاهدة مريحة ليلًا ونهارًا
- 📊 **تقارير مالية شاملة** — دخل الاشتراكات، الدخل الآخر، إجمالي الدخل، المصروفات، صافي الربح، عدد الفواتير
- 📋 **تقرير المديونين** — متابعة المدفوعات المستحقة وديون العملاء
- 📅 **تصفية حسب التاريخ** — تقارير شهرية أو نطاقات تاريخ مخصصة
- 🖨️ **تصدير وطباعة** — طباعة PDF وتصدير Excel بنقرة واحدة
- 💵 **طرق دفع متعددة** — تتبع النقدية والتحويل البنكي
- 👥 **صلاحيات حسب الدور** — حسابات مدير وجامع فواتير بصلاحيات مختلفة
- 📱 **وصول عبر الشبكة** — استخدم التطبيق من أي جهاز على نفس الشبكة المحلية

---

## 🚀 Getting Started / التشغيل

### English

1. Clone the repository:

   ```bash
   git clone https://github.com/melsebaey/isp-billing.git
   cd isp-billing
   ```

2. Double-click on the **`start.bat`** file to launch the application.

   > ⚠️ **Warning:** Do not close the terminal (Command Prompt) window while the application is running, otherwise the server will stop.

### العربية

1. استنسخ المستودع:

   ```bash
   git clone https://github.com/melsebaey/isp-billing.git
   cd isp-billing
   ```

2. انقر مرتين على الملف **`start.bat`** لتشغيل التطبيق.

   > ⚠️ **تنبيه:** لا تُغلق نافذة موجه الأوامر (Terminal) أثناء تشغيل التطبيق، وإلا سيتوقف الخادم.

---

## 🌐 Accessing the Application / الوصول إلى التطبيق

### English

After running `start.bat`, open your browser and enter one of the following addresses:

| Access Type | URL |
|-------------|-----|
| 🖥️ Local | `http://localhost:8080` |
| 📡 Network | `http://your-pc-ip:8080` |

> 💡 **Replace** `your-pc-ip` with your computer's IP address on the local network.

### العربية

بعد تشغيل `start.bat`، افتح متصفحك وأدخل أحد العناوين التالية:

| نوع الوصول | الرابط |
|------------|-------|
| 🖥️ محلي (Local) | `http://localhost:8080` |
| 📡 عبر الشبكة | `http://your-pc-ip:8080` |

> 💡 **استبدل** `your-pc-ip` بعنوان IP الخاص بجهازك على الشبكة المحلية.

---

## 🔐 Default Login Credentials / بيانات الدخول الافتراضية

### 👑 Admin Account / حساب المدير

| Field / الحقل | Value / القيمة |
|---------------|----------------|
| Username / اسم المستخدم | `admin` |
| Password / كلمة المرور | `123456` |

### 💼 Collector Account / حساب جامع الفواتير

| Field / الحقل | Value / القيمة |
|---------------|----------------|
| Username / اسم المستخدم | `user` |
| Password / كلمة المرور | `123456` |

> 🔒 **Security / أمان:** It is recommended to change the default passwords immediately after the first login. / يُنصح بتغيير كلمات المرور الافتراضية فور تسجيل الدخول الأول للحفاظ على أمان النظام.

---

## 📱 Network Access / الوصول عبر الشبكة

### English

You can access the application from **any computer or mobile device** connected to the same local network (Wi-Fi / LAN) by entering:

```
http://your-pc-ip:8080
```

in the browser of the device you are using.

### العربية

يمكنك الوصول إلى التطبيق من **أي جهاز كمبيوتر أو هاتف محمول** متصل بنفس الشبكة المحلية (Wi-Fi / LAN)، وذلك عبر إدخال:

```
http://your-pc-ip:8080
```

في متصفح الجهاز المستخدم.

---

## 🧩 Application Modules / وحدات التطبيق

### English

The application's sidebar includes the following modules:

| Module | Description |
|--------|-------------|
| 🏠 **Home** | Dashboard with key metrics and overview |
| 👤 **Users** | Manage customer accounts and information |
| 📦 **Packages** | Define and manage subscription packages |
| 💼 **Accounts** | Financial accounts management |
| 🧾 **Invoices** | Create and track customer invoices |
| 💳 **Payments** | Record and review payments (cash / bank) |
| 💸 **Expenses** | Track operational expenses by category |
| 📊 **Reports** | Comprehensive Financial Report & Debtors Report |
| 🛠️ **Technical Support** | Customer support tickets management |
| ⚙️ **Settings** | Application configuration and preferences |

### العربية

يحتوي الشريط الجانبي للتطبيق على الوحدات التالية:

| الوحدة | الوصف |
|--------|-------|
| 🏠 **الرئيسية** | لوحة تحكم بالمؤشرات الرئيسية ونظرة عامة |
| 👤 **المستخدمون** | إدارة حسابات العملاء ومعلوماتهم |
| 📦 **الباقات** | تعريف وإدارة باقات الاشتراك |
| 💼 **الحسابات** | إدارة الحسابات المالية |
| 🧾 **الفواتير** | إنشاء وتتبع فواتير العملاء |
| 💳 **المدفوعات** | تسجيل ومراجعة المدفوعات (نقدي / بنكي) |
| 💸 **المصروفات** | تتبع المصروفات التشغيلية حسب الفئة |
| 📊 **التقارير** | التقرير المالي الشامل وتقرير المديونين |
| 🛠️ **الدعم الفني** | إدارة تذاكر دعم العملاء |
| ⚙️ **الإعدادات** | إعدادات التطبيق والتخصيص |

### 📊 Reports Page Preview / معاينة صفحة التقارير

The **Reports** module provides a comprehensive financial overview including:

- **Statistics Cards** — Subscription Income, Other Income, Total Income, Total Expenses, Net Profit, Invoices Count
- **Detailed Breakdown Table** — Income sources, expenses, total billing, outstanding debts
- **Payment Methods** — Cash and Bank Transfer distribution
- **Date Filtering** — Monthly or custom date ranges
- **Export Options** — Print to PDF and Export to Excel

> 💡 Currency: **Egyptian Pound (ج.م)** / العملة: **الجنيه المصري (ج.م)**

---

## ⚙️ Requirements / المتطلبات

### English

- Operating System: Windows
- A modern web browser (Chrome / Edge / Firefox / Safari)
- A local network connection (to access from other devices)

### العربية

- نظام تشغيل: Windows
- متصفح إنترنت حديث (Chrome / Edge / Firefox / Safari)
- اتصال بشبكة محلية (للوصول من أجهزة أخرى)

---

## 🛠️ Troubleshooting / استكشاف الأخطاء

### English

| Problem | Solution |
|---------|----------|
| Page does not open | Make sure the `start.bat` window is not closed |
| Cannot access from another device | Verify both devices are on the same network and check the IP address |
| Port 8080 is in use | Stop other applications using the same port and restart |
| Reports show no data | Select a valid date range and ensure invoices/payments exist |

### العربية

| المشكلة | الحل |
|---------|------|
| الصفحة لا تفتح | تأكد من عدم إغلاق نافذة `start.bat` |
| لا يمكن الوصول من جهاز آخر | تحقق من اتصال الجهازين بنفس الشبكة ومن عنوان IP |
| المنفذ 8080 مستخدم | أوقف التطبيقات التي تستخدم نفس المنفذ وأعد التشغيل |
| التقارير لا تعرض بيانات | اختر نطاق تاريخ صحيحًا وتأكد من وجود فواتير ومدفوعات |

---

## 📞 Support / الدعم

### English

For technical support or to report an issue, please open a new [Issue](https://github.com/melsebaey/isp-billing/issues) on GitHub.

### العربية

للدعم الفني أو الإبلاغ عن مشكلة، يرجى فتح [Issue جديد](https://github.com/melsebaey/isp-billing/issues) على GitHub.

---

<div align="center">

**© 2026 ISP Billing — All Rights Reserved / جميع الحقوق محفوظة**

</div>
