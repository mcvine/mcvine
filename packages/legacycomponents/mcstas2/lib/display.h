// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2005 All Rights Reserved  
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#ifndef H_MCSTAS2_DISPLAY
#define H_MCSTAS2_DISPLAY

void mcdis_magnify(char *);
void mcdis_line(double, double, double, double, double, double);
void mcdis_dashed_line(double, double, double, double, double, double, int);
void mcdis_rectangle(char *, double, double, double, double, double);
void mcdis_box(double, double, double, double, double, double);
void mcdis_circle(char *, double, double, double, double);
void mcdis_multiline(int, ...);


namespace mcstas2 {
  void multiline(int, ...);
  inline void magnify(char *c) {mcdis_magnify(c);}
  inline void line(double x1, double y1, double z1, double x2, double y2, double z2) {mcdis_line(x1,y1,z1, x2,y2,z2);}
  inline void dashed_line(double x1, double y1, double z1, double x2, double y2, double z2, int n) {mcdis_dashed_line(x1,y1,z1, x2,y2,z2, n);}
  inline void rectangle(char *plane, double x, double y, double z, double width, double height) {mcdis_rectangle(plane, x,y,z, width,height);}
  inline void box(double x, double y, double z, double w, double h, double l) {mcdis_box(x,y,z, w,h,l);}
  inline void circle(char *plane, double x, double y, double z, double r) {mcdis_circle(plane, x,y,z, r);}
}


#endif // H_MCSTAS2_DISPLAY
