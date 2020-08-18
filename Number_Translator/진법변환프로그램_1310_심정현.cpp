#include <stdio.h>
#define ERR -2
int trans(char *from, int demical); // convert input to demical number function
void converter(int result, int re); // convert demical number function

int main(){
	int demical, result, re;
	char from[30];
	while(1){
		printf("[진수]\n>> ");
		scanf("%d", &demical);
		printf("\nSaved 진수: %d\n", demical);
		printf("\n[변환 할 입력값]\n>> ");
		if(demical==2||demical==8||demical==10||demical==16){ // 진수 입력값 제한 
			scanf("%s", from);
			printf("\n[변환할 진법]\n>> ");
			scanf("%d", &re);
			result=trans(from, demical);
			if(result<0){
				printf("\nInput Error");
				return 0; 
			}
			converter(result, re);
		}
		else{
			printf("\nInput Error");
			return 0;
		}
	}
	return 0;
}

int trans(char *from, int demical){
	int temp=0, i;
	for(i=0;from[i]!='\0';i++){
		if(from[i]>='0'&&from[i]<='9'){ // 입력값이 0~9일 때 10진수로 변환 
			from[i]-='0';
		}
		else if(from[i]>='A'&&from[i]<='F'){ // 입력값이 A~F일 때 10진수로 변환 
			from[i]-='A';
			from[i]+=10;
		}
		if(from[i]>=demical) return ERR; // check the input error
		temp*=demical; // 최종 변환 코드 
		temp+=from[i];
		if(temp>65535) return ERR; // check the input error
	}
	return temp;
}

void converter(int result, int re){
	int i, m=28;
	char changed[30];
	for(i=0;i<30;i++){
		changed[i]=-1; // 변환값을 저장할 배열을 -1로 초기화 
	}
	for(i=re;result>0;){
		changed[m--]=result%re; // 입력 받은 진수로 변환하는 코드 
		result/=re;
	}
	printf("\n결과: "); 
	for(i=m+1;changed[i]!=-1;i++){  
		if(changed[i]>=0&&changed[i]<=9){ // 변환된 값이 0~9일 때 변환 코드 
			changed[i]+='0';
		}
		else if(changed[i]>=10&&changed[i]<=15){ // 변환된 값이 A~F일 때 변환 코드 
			changed[i]-=10;
			changed[i]+='A';
		}
		printf("%c", changed[i]);
	}
	printf("\n\n");
}
