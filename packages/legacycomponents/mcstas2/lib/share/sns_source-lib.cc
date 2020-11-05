/*
 * Author: Garrett Granroth
 * Extracted from SNS_source components and Adapted to MCViNE by Jiao Lin
 */

#include "mcstas2/exception.h"
#include "sns_source-lib.h"

namespace mcstas2 { namespace SNSsource {

  /* ----------------------------------------------------------------
     routine to load E, I and t I data from SNS source files
     -----------------------------------------------------------------*/
  void sns_source_load(char filename[], double *xvec, double *yvec, int xcol, int ycol, int *veclenptr, double *tcol, double *Ecol, double **Imat,int *ntvals, int *nEvals)
  {
    FILE *fp;
    int idx1,idx2,idx3; /* counter for number of x, y values */
    int jk, idx3max;
    int numtvals;
    int totalvals;
    float indat[6];
    double *Icoltmp, *tcoltmp, *Ecoltmp;
    char *line;
    char *lntoken, *cp;
    Icoltmp=(double *)malloc(100000*sizeof(double));
    tcoltmp=(double *)malloc(100000*sizeof(double));
    Ecoltmp=(double *)malloc(100000*sizeof(double));
    line=(char *)malloc(200*sizeof(char));
    /* open file */
    printf("%s\n",filename);
    fp=fopen(filename,"r");
    if (fp==NULL){
      printf("Error opening file");
      mcstas2::exit(-1);
      }
    /* skip header lines any line that begin with # */
    while((fgets(line,Maxlength,fp)!=NULL)&&(strchr(line,'#')!=NULL)){      
    }
    /* need code to back up one line */
    idx1=0;  
    /* read all lines that fit the format for the time integrated data*/
    while(sscanf(line," %f %f %f %f %f %f",&indat[0], &indat[1], &indat[2], &indat[3],&indat[4],&indat[5])>0){
      xvec[idx1]=indat[xcol];
      yvec[idx1]=indat[ycol];
      //printf("idx1 %i xvec %g yvec %g\n",idx1,xvec[idx1],yvec[idx1]);
      idx1++;
      fgets(line,Maxlength,fp);
    }
    idx1--;   // correct index since it counts one line past useful data
    // printf("idx1 %i\n",idx1);
    idx2=floor(idx1/2);
    while((idx2<idx1)&&(yvec[idx2]>0)){
      idx2++;
    }
    if(idx2<idx1){
      *veclenptr=idx2;
    }
    else{
      *veclenptr=idx1-2; 
    }
  /* find t data header */
    fgets(line,Maxlength,fp);
    while(strrchr(line,'#')==NULL){
      fgets(line,Maxlength,fp);
    }
  /*find end of E data header */
    while((fgets(line,Maxlength,fp)!=NULL)&&(strchr(line,'#')!=NULL)){      
    }
  /* read in t data */
 /*printf("t data read start\n");*/
    idx2=0;
    //while(fgets(line,Maxlength,fp)!=NULL){    
    do {
      jk=sscanf(line," %f %f %f %f",&indat[0], &indat[1], &indat[2], &indat[3]);
      if ((line!=NULL)&&(jk>3)){
        tcoltmp[idx2]=indat[0];
        Ecoltmp[idx2]=indat[1];
        Icoltmp[idx2]=indat[2];
        //printf("%d %d %g %g %g %g\n",idx2,jk,tcoltmp[idx2],Ecoltmp[idx2],Icoltmp[idx2],indat[3]);
        idx2++;
        }
     } while (fgets(line,Maxlength,fp)!=NULL);
    fclose(fp);
    totalvals=idx2+1;
    // totalvals=idx2;
    printf("total vals: %d\n",totalvals);
    /* reformat data into an Ecol, a tcol, and an I matrix*/
    idx1=0;idx2=0;idx3=0;
    Ecol[idx2]=Ecoltmp[idx1];
    tcol[idx3]=tcoltmp[idx1];
    Imat[idx3][idx2]=Icoltmp[idx1];
    idx1++;idx3++;

    printf("idx3 = %d\n", idx3);
    printf("totalvals = %d\n", totalvals);
    printf("Ecoltmp[0] = %g\n", Ecoltmp[0]);
    printf("tcoltmp[0] = %g\n", tcoltmp[0]);

    while(idx1<totalvals){
      jk=idx1-1;
      if(Ecoltmp[idx1]==Ecoltmp[jk]){
        tcol[idx3]=tcoltmp[idx1];
         Imat[idx3][idx2]=Icoltmp[idx1];
         idx1++;idx3++;
      }
      else{
	//printf("idx1 = %d, idx3 = %d \n", idx1, idx3);
        idx3max=idx3;
        idx2++;idx3=0;
        Ecol[idx2]=Ecoltmp[idx1];
        tcol[idx3]=tcoltmp[idx1];
        Imat[idx3][idx2]=Icoltmp[idx1];
        idx1++;idx3++;
      }
    }
   *ntvals=idx3max+1;*nEvals=idx2;
   printf("ntvals: %i idx: %i\n",*ntvals, idx3);
   free(Icoltmp);free(tcoltmp);free(Ecoltmp);free(line);
  }
  /*-------------------------------------------------------------
    End load file routines
    --------------------------------------------------------------*/  
  /*----------------------------------------------------------------------
    routine to do a 1D linear interpolation
    ------------------------------------------------------------------------*/
  /* given a point (x1,y1) on the low side of xdes and one (x2,y2) on the
     high side of xdes return the interpolated y values */
  double linint(double xdes,double x1, double x2, double y1, double y2)
  {
    double m;
    m=(y2-y1)/(x2-x1);
    return (m*(xdes-x1)+y1);
  }

  double linfuncint(double xdes, double xylen, double *vecx, double *vecy)
  {
    int idx;
    idx=0;
    while((vecx[idx]<xdes)&&idx<xylen){
      idx++;
    }
    if (idx>xylen){
      printf("error exceeded vector length");
    }
    if (vecx[idx]==xdes){
      return vecy[idx];
    }
    else
      {
        return linint(xdes,vecx[idx-1],vecx[idx],vecy[idx-1],vecy[idx]);
      }
  }
  /*------------------------------------------------------------------------
    routine to perform a 1 d quadratic interpolation 
    --------------------------------------------------------------------------*/
  /* given 2 points on the low side of xdes and one on the high side, return
     a quadratically interpolated result */
  double quadint(double xdes,double x1, double x2,double x3, double y1, double
                 y2, double y3)
  {
    double t1, t2, t3;
    t1=((xdes-x2)*(xdes-x3)*y1)/((x1-x2)*(x1-x3));
    t2=((xdes-x1)*(xdes-x3)*y2)/((x2-x1)*(x2-x3));
    t3=((xdes-x1)*(xdes-x2)*y3)/((x3-x1)*(x3-x2));
    return t1+t2+t3; 
  }

  double quadfuncint(double xdes, double xylen, double *vecx, double *vecy)
  {
    int idx;
    idx=1;
    while((vecx[idx]<xdes)&&idx<xylen){
      idx++;
    }
    if (idx>xylen){
      printf("error exceeded vector length");
    }

    if (vecx[idx]==xdes){
      return vecy[idx]; 
    }
    else
      {
        return quadint(xdes,vecx[idx-2],vecx[idx-1],vecx[idx],vecy[idx-2],vecy[idx-1],vecy[idx]);
      }
  }
  /*-------------------------------------------------------------------
    integration routines
    ---------------------------------------------------------------------*/
  double integtrap(const F1 & func,double prev,double low,double high, int step)
  {
    double s,npts,stpsze,sum,x;
    int pw2, idx;
    if (step==1){
      return(s=0.5*(high-low)*(func(high)+func(low)));
    }
    else{
      s=prev;
      for(pw2=1,idx=1;idx<step-1;idx++){
        pw2<<=1;
      } 
      npts=pw2;
      stpsze=(high-low)/npts;
      x=low+0.5*stpsze;
      for(sum=0.0,idx=1;idx<=pw2;idx++,x+=stpsze){
        sum+=func(x);
      }
      s=0.5*(s+(high-low)*sum/npts);
      return s;
    }
  }
  double integ1(const F1& func,double low, double high, double err)
  { 
    double out,outprev;
    int idx;
    out=integtrap(func,0.0,low,high,1);
    outprev=out;  
    out=integtrap(func,out,low,high,2);
    /*printf("out %g outprev %g \n",out,outprev);*/
    idx=2;
    while(fabs(out-outprev)>err*fabs(out)){
      idx++;
      outprev=out;
      out=integtrap(func,out,low,high,idx);
      /* printf("out %g outprev %g \n",out,outprev);*/
    }
    return out;
  }
  /*---------------------------------------------------------------------------
    Routine for finding zeros. 
    Modified version of rtbis from "Numerical Recipes in C: pg 354
    -----------------------------------------------------------------------------*/
  double zero_find(const F2 &func,double yval,double xmin,double xmax, double tol)
  {
    double xl,xh,f,fmid,xmid,dx,rtb;
    xl=xmin;
    xh=pow(10,(log10(xmin)+yval*(log10(xmax)-log10(xmin))));
    f=func(xl,yval);
    fmid=func(xh,yval);
    while (fmid*f>=0.0){
      xh=xh+(xh-xl)*2.0;
      fmid=func(xh,yval);
    }
    dx=xh-xl;
    rtb=xl;
    while(fabs(func(rtb,yval))>tol){
      dx=dx*0.5;
      xmid=rtb+dx;
      fmid=func(xmid,yval);
      if (fmid<0){
        rtb=xmid;
      }
    }
    return rtb;
  }
  /*----------------------------------------------------------------------------
    Routine for calculating Probability distribution
    ----------------------------------------------------------------------------*/
  void Pcalc(const F1 &func,double llim, double hlim, double *xvec, double *Prob, int veclen, int *idxstart, int *idxstop)
  {
    int idx1,idx2;
    double junk,Norm;
    idx1=0;
    while(xvec[idx1]<=llim){
      Prob[idx1]=0;
      idx1++;
    }
    if (idx1<1){
      printf("Error: lower energy limit is out of bounds\n");
      mcstas2::exit(0);
    }
    *idxstart=idx1;  
    Prob[idx1]=integ1(func,llim,xvec[idx1],0.001);
    idx1++;
    while(xvec[idx1]<=hlim){    
      junk=integ1(func,xvec[idx1-1],xvec[idx1],0.001);     
      Prob[idx1]=(Prob[idx1-1]+junk);    
      idx1++;    
    }
    *idxstop=idx1;
    while(idx1<veclen){
      Prob[idx1]=1;
      idx1++;
    }
  /*Normalize all Probability values*/
    Norm=Prob[*idxstop-1];
    if (Norm>0){
      for(idx2=*idxstart;idx2<*idxstop;idx2++){
        Prob[idx2]=Prob[idx2]/Norm;
      }
    }
  }
  /*----------------------------------------------------------------------------
    Routine for calculating t Probability distribution
    ----------------------------------------------------------------------------*/
  void tPcalc(const F1 &func,double llim, double hlim, double *xvec, double *Prob, int veclen, int *idxstart, int *idxstop)
  {
    int idx1,idx2;
    double junk,Norm;
    idx1=0;
    while(xvec[idx1]<=llim){
      Prob[idx1]=0;
      idx1++;
    }
    *idxstart=idx1;  
    Prob[idx1]=integ1(func,llim,xvec[idx1],0.001);
    while(xvec[idx1]<=hlim){    
      junk=integ1(func,xvec[idx1-1],xvec[idx1],0.001);
      Prob[idx1]=(Prob[idx1-1]+junk);
      idx1++;    
    }
    *idxstop=idx1;
    while(idx1<veclen){
      Prob[idx1]=1;
      idx1++;
    }
    /* calculate normalization*/
    Norm=Prob[*idxstop-1];
    /*printf("Norm %f\n",Norm); */
    /*Normalize all Probability values*/
    if (Norm>0){
      for(idx2=*idxstart;idx2<*idxstop;idx2++){
        Prob[idx2]=Prob[idx2]/Norm;
        /*printf("%d %g \n",idx2,Prob[idx2])*/;
      }
    }
  }

}}
